# self_rag.py
import os, re, json, glob
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from dotenv import load_dotenv
from .SF_prompts import PROMPT_RELEVANCE_GRADER, PROMPT_SUPPORT_CHECKER, PROMPT_UTILITY_GRADER, PROMPT_GENERATE_COMMANDS, PROMPT_CRITIQUE
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool

try:
    from pypdf import PdfReader
    _PDF_OK = True
except Exception:
    _PDF_OK = False


# ------------------------------- Utils -------------------------------

def _read_file(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in {".txt", ".md", ".log", ".cfg", ".conf"}:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        if ext in {".pdf"} and _PDF_OK:
            reader = PdfReader(path)
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        # fallback: prova comunque come testo
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


def _json_first_obj(s: str) -> Optional[dict]:
    """estrai il primo blocco JSON valido da una stringa"""
    try:
        return json.loads(s)
    except Exception:
        pass
    try:
        start = s.find("{")
        end = s.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(s[start:end+1])
    except Exception:
        return None
    return None


# --------------------------- Data structures -------------------------

@dataclass
class RetrievalResult:
    content: str
    score: float
    metadata: dict


class SelfRAGInput(BaseModel):
    query: str = Field(description="Query dell'agente.")
    shared_report: str = Field(description="Report condiviso (JSON o testo).")
    agent_role: str = Field(description="Ruolo agente che invoca (Reconnaissance, Scanning, Exploitation, PrivEsc).")


# ------------------------------ Self-RAG -----------------------------

class SelfRAG:
    """
    Implementazione Self-RAG *funzionante*:
    - build_vector_db(path, kb_name, persist_dir): genera KB per cartella (FAISS + OpenAIEmbeddings)
    - build_all_from_root(root): per ogni sottocartella crea una KB col nome della cartella
    - run(query, shared_report, agent_role): esegue i pilastri e restituisce comandi anti-allucinazione
    - get_tool(): espone un StructuredTool integrabile nei tuoi agenti LangGraph
    """

    def __init__(
        self,
        embedding_model: str = "text-embedding-3-small",
        llm_model: str = "gpt-5",
        persist_root: str = "vector_dbs",
        k: int = 5,
        rel_threshold: float = 0.0
    ):
        load_dotenv()
        self.emb = OpenAIEmbeddings(model=embedding_model)
        self.llm = ChatOpenAI(model=llm_model, temperature=0)
        self.persist_root = persist_root
        self.k = k
        self.rel_threshold = rel_threshold
        self.vector_dbs: Dict[str, FAISS] = {}   # kb_name -> FAISS

        os.makedirs(self.persist_root, exist_ok=True)

    # ------------------------- KB builders -------------------------

    def build_vector_db(self, path: str, kb_name: str) -> None:
        """
        Carica tutti i file nella cartella `path`, fa chunking e crea FAISS,
        salvando su disco in persist_root/kb_name
        """
        files = [p for p in glob.glob(os.path.join(path, "**/*"), recursive=True) if os.path.isfile(p)]
        texts: List[Document] = []
        for fp in files:
            content = _read_file(fp)
            if not content.strip():
                continue
            texts.append(Document(page_content=content, metadata={"source": fp}))

        if not texts:
            raise RuntimeError(f"Nessun documento valido in {path}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=150)
        chunks = splitter.split_documents(texts)

        vs = FAISS.from_documents(chunks, self.emb)
        kb_dir = os.path.join(self.persist_root, kb_name)
        os.makedirs(kb_dir, exist_ok=True)
        vs.save_local(kb_dir)
        self.vector_dbs[kb_name] = vs
        print(f"[SelfRAG] KB '{kb_name}' costruita con {len(chunks)} chunk. Persist: {kb_dir}")

    def load_vector_db(self, kb_name: str) -> None:
        kb_dir = os.path.join(self.persist_root, kb_name)
        if not os.path.isdir(kb_dir):
            raise FileNotFoundError(f"KB '{kb_name}' non trovata in {kb_dir}")
        self.vector_dbs[kb_name] = FAISS.load_local(kb_dir, self.emb, allow_dangerous_deserialization=True)

    def build_all_from_root(self, root: str) -> List[str]:
        """
        Per ogni sottocartella di `root` crea una KB con lo stesso nome.
        Ritorna la lista dei kb_name creati.
        """
        created = []
        for name in sorted(os.listdir(root)):
            sub = os.path.join(root, name)
            if os.path.isdir(sub):
                self.build_vector_db(sub, name)
                created.append(name)
        return created

    # --------------------- Self-RAG pillars ------------------------

    def retrieve_decision(self, query: str, shared_report: str, agent_role: str) -> bool:
        """
        Decide (LLM) se fare retrieval.
        """
        return True

    def retrieve(self, query: str, kb_name: str) -> List[RetrievalResult]:
        if kb_name not in self.vector_dbs:
            # prova a caricare da disco
            try:
                self.load_vector_db(kb_name)
            except Exception:
                return []
        vs = self.vector_dbs[kb_name]
        hits = vs.similarity_search_with_score(query, k=self.k)
        return [
            RetrievalResult(content=h[0].page_content, score=float(h[1]), metadata=h[0].metadata or {})
            for h in hits
        ]

    def relevance_grader(self, query: str, passages: List[RetrievalResult]) -> List[RetrievalResult]:
        """
        Filtra passaggi non rilevanti (LLM). Mantieni quelli con label 'RELEVANT'.
        """
        if not passages:
            return []
        sys = PROMPT_RELEVANCE_GRADER
        kept: List[RetrievalResult] = []
        for p in passages:
            prompt = f"Query: {query}\nPassage:\n{p.content[:1500]}\nLabel:"
            try:
                lab = self.llm.invoke([("system", sys), ("user", prompt)]).content.strip().upper()
                if "RELEVANT" in lab:
                    kept.append(p)
            except Exception:
                # fallback: tieni tutti
                kept.append(p)
        return kept

    def support_checker(self, query: str, passages: List[RetrievalResult], answer: str) -> bool:
        """
        Verifica che l'output sia supportato dai passaggi (LLM → 'SUPPORTED'/'UNSUPPORTED').
        """
        sys = PROMPT_SUPPORT_CHECKER
        ctx = "\n---\n".join(p.content[:1200] for p in passages)
        hp = f"QUERY:\n{query}\n\nEVIDENZE:\n{ctx}\n\nOUTPUT:\n{answer}\n\nVerdetto:"
        try:
            res = self.llm.invoke([("system", sys), ("user", hp)]).content.strip().upper()
            return "SUPPORTED" in res
        except Exception:
            return bool(passages)

    def utility_grader(self, query: str, answer: str) -> int:
        """
        Grado di utilità 1..5 (LLM). Fallback: len(answer).
        """
        sys = PROMPT_UTILITY_GRADER
        hp = f"QUERY:\n{query}\n\nOUTPUT:\n{answer}\n\nVOTO:"
        try:
            raw = self.llm.invoke([("system", sys), ("user", hp)]).content.strip()
            m = re.search(r"([1-5])", raw)
            return int(m.group(1)) if m else 3
        except Exception:
            return 3 if len(answer) > 80 else 2

    def generate_commands(self, query: str, shared_report: str, agent_role: str, passages: List[RetrievalResult]) -> Dict[str, Any]:
        """
        Genera **SOLO JSON** con comandi suggeriti (1-3), ciascuno con rationale e confidence.
        Obbliga l'LLM a citare evidenze sintetiche (anti-allucinazione).
        """
        sys = PROMPT_GENERATE_COMMANDS
        ctx = "\n---\n".join(p.content[:1000] for p in passages) if passages else "(nessuna evidenza)"
        hp = (
            f"ROLE: {agent_role}\n"
            f"QUERY: {query}\n"
            f"REPORT:\n{shared_report}\n\n"
            f"EVIDENZE:\n{ctx}\n\n"
            "RISPONDI SOLO CON JSON."
        )
        out = self.llm.invoke([("system", sys), ("user", hp)]).content
        data = _json_first_obj(out) or {"commands": [], "notes": "no-json"}
        # normalizza
        cmds = []
        for c in data.get("commands", []):
            if not isinstance(c, dict): 
                continue
            cmd = c.get("cmd") or c.get("command") or ""
            if not cmd.strip():
                continue
            cmds.append({
                "cmd": cmd.strip(),
                "rationale": (c.get("rationale") or "")[:300],
                "confidence": int(c.get("confidence") or 50)
            })
        data["commands"] = cmds[:3]
        return data

    def critique(self, query: str, shared_report: str, agent_role: str, draft: Dict[str, Any], passages: List[RetrievalResult]) -> Dict[str, Any]:
        """
        Critica e migliora (LLM) la lista comandi (riduzione rischi, +evidenze).
        Ritorna lo stesso schema JSON.
        """
        sys = PROMPT_CRITIQUE
        ctx = "\n---\n".join(p.content[:800] for p in passages) if passages else "(nessuna evidenza)"
        hp = (
            f"ROLE: {agent_role}\nQUERY: {query}\nREPORT:\n{shared_report}\n\n"
            f"EVIDENZE:\n{ctx}\n\n"
            f"DRAFT:\n{json.dumps(draft, ensure_ascii=False)}\n\n"
            "RISPONDI SOLO CON JSON."
        )
        out = self.llm.invoke([("system", sys), ("user", hp)]).content
        data = _json_first_obj(out) or draft
        # normalizza
        cmds = []
        for c in data.get("commands", []):
            if not isinstance(c, dict): 
                continue
            cmd = c.get("cmd") or c.get("command") or ""
            if not cmd.strip():
                continue
            cmds.append({
                "cmd": cmd.strip(),
                "rationale": (c.get("rationale") or "")[:300],
                "confidence": int(c.get("confidence") or 50)
            })
        data["commands"] = cmds[:3]
        return data

    # ------------------------- Orchestrator -------------------------

    def run(self, query: str, shared_report: str, agent_role: str) -> Dict[str, Any]:
        """
        Pipeline completa Self-RAG.
        Ritorna un dict con:
          - commands: [{cmd, rationale, confidence}]
          - supported: bool
          - utility: int(1..5)
          - notes: str
        """
        # 1) Retrieve decision
        #do_ret = self.retrieve_decision(query, shared_report, agent_role)
        #mi forzo il retrieve
        do_ret = True
        # 2) Retrieval
        passages: List[RetrievalResult] = []
        if do_ret:
            kb_name = agent_role if agent_role in self.vector_dbs or os.path.isdir(os.path.join(self.persist_root, agent_role)) else None
            if kb_name:
                passages = self.retrieve(query, kb_name)

        # 3) Relevance grading
        passages = self.relevance_grader(query, passages)

        # 4) First draft commands
        draft = self.generate_commands(query, shared_report, agent_role, passages)

        # 5) Support check & optional refine
        supported = self.support_checker(query, passages, json.dumps(draft, ensure_ascii=False))
        refined = self.critique(query, shared_report, agent_role, draft, passages) if not supported else draft

        # 6) Utility grading
        utility = self.utility_grader(query, json.dumps(refined, ensure_ascii=False))
        print('*'*20)
        print(f"[SelfRAG] Retrieved {len(passages)} passages. Supported: {supported}. Utility: {utility}/5.")
        print(f"[SelfRAG] Commands: {refined.get('commands', [])}. Notes: {refined.get('notes', '')}")
        print('*'*20)
        return {
            "commands": refined.get("commands", []),
            "supported": supported,
            "utility": utility,
            "notes": refined.get("notes", "")
        }

    # ------------------------ LangChain Tool ------------------------

    def get_tool(self) -> StructuredTool:
        """
        Ritorna un StructuredTool integrabile nei tuoi agenti.
        """
        rag = self

        def _tool_fn(query: str, shared_report: str, agent_role: str) -> Dict[str, Any]:
            return rag.run(query=query, shared_report=shared_report, agent_role=agent_role)

        return StructuredTool.from_function(
            func=_tool_fn,
            name="self_rag_tool",
            description="SELF-RAG: recupera conoscenza dalla KB per ruolo e propone 1-3 comandi fondati su evidenze.",
            args_schema=SelfRAGInput
        )


# ------------------------------ MAIN --------------------------------
self_rag_tool = StructuredTool.from_function(
    func=SelfRAG().run,
    name="self_rag_tool",
    description="🔍 SELF-RAG TOOL - Suggerisce comandi utili per la fase di reconnaissance.",
    args_schema=SelfRAGInput
)
if __name__ == "__main__":
    """
    Test rapido: 
    - metti i tuoi file in ./kb/Reconnaissance e ./kb/Scanning (una cartella per ruolo)
    - imposta PROMPT, ROLE, REPORT qui sotto
    - esegui: python self_rag.py
    """
    load_dotenv()
    rag = SelfRAG()

    # 1) Costruisci KB per ogni sottocartella di ./kb (nome cartella = kb_name = ruolo)
    kb_root = "./kb"
    if os.path.isdir(kb_root):
        created = rag.build_all_from_root(kb_root)
        print(f"[SelfRAG] KB create: {created}")
    else:
        print("[SelfRAG] Nessuna cartella ./kb trovata. Creala per usare il retrieval per-ruolo.")

    # 2) Parametri di test (come se fosse un agente che invoca)
    PROMPT = "Voglio enumerare rapidamente i servizi; quali comandi usare su questo target?"
    ROLE   = "Reconnaissance"  # oppure "Scanning", "Exploitation", "PrivilegeEscalation"
    REPORT = '{"target":"127.0.0.1","services":[{"port":80,"service":"http"}],"os":"windows"}'

    # 3) Esegui Self-RAG
    result = rag.run(query=PROMPT, shared_report=REPORT, agent_role=ROLE)

    print("\n=== SELF-RAG RESULT ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    """
    # 4) Se vuoi il tool per LangGraph:
    tool = rag.get_tool()
    # Esempio invocazione tool:
    tool_out = tool.run({"query": PROMPT, "shared_report": REPORT, "agent_role": ROLE})
    print("\n=== TOOL OUTPUT ===")
    print(json.dumps(tool_out, indent=2, ensure_ascii=False))
    """