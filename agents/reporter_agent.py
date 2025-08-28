# agents/reporter_agent.py  (oppure incolla in core_agent.py al posto del reporter attuale)
import json, os, re
from typing import TypedDict, Annotated, Sequence
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage, AIMessage
from langgraph.graph.message import add_messages

from prompts import REPORTER_AGENT_PROMPT
from .state import AgentState

# ---- schema base del report condiviso ----
def _default_report():
    return {
        "target": '',
        "phases": [],     # es: ["Reconnaissance", "Scanning"]
        "found_credentials":[],                    
        "services": [],                       # es: [{"port":80,"service":"http","version":"Apache 2.4.18"}]
        "web_findings": {"dirs": [], "alerts": []},
        "vuln_hypotheses": [],                # es: ["Apache 2.4.18 outdated"]
        "access": {"user_shell": False, "privs": "none"},
        "OS":'',
        "flags_found": 0,
        "notes": [],                         
        "wrong_paths":[],
        "next_phase_hint": None               # suggerimento dell'agente di fase
    }

def _safe_load_report(s: str) -> dict:
    try:
        data = json.loads(s) if s and s.strip() else _default_report()
        # sanity check minima
        if not isinstance(data, dict): 
            return _default_report()
        return data
    except Exception:
        return _default_report()

def _detect_phase(text: str) -> str | None:
    # es. "[Reconnaissance] ..." → "Reconnaissance"
    m = re.match(r"\s*\[([^\]]+)\]", text or "")
    return m.group(1) if m else None

def reporter_agent(state: AgentState) -> AgentState:
    """
    LLM Reporter:
    - prende shared_report (JSON) + ultimo messaggio dell'agente
    - aggiorna il report (merge, dedup, niente invenzioni)
    - restituisce lo shared_report aggiornato nello state
    """
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    prev_report = _safe_load_report(state.get("shared_report", ""))
    last_msg = state["messages"][-1]
    agent_output = last_msg.content if hasattr(last_msg, "content") else str(last_msg)
    phase = _detect_phase(agent_output)

    # prompt: chiediamo SOLO JSON aggiornato, rispettando lo schema
    system = SystemMessage(content=REPORTER_AGENT_PROMPT)

    human = HumanMessage(content=(
        "Report corrente (JSON):\n"
        f"{json.dumps(prev_report, ensure_ascii=False)}\n\n"
        f"Fase corrente: {phase or 'unknown'}\n"
        "Nuovo output dell'agente (stringa):\n"
        f"{agent_output}\n\n"
        "Restituisci SOLO il JSON aggiornato."
    ))

    # invoco l'LLM e cerco di parsare un JSON pulito
    resp = model.invoke([system, human])
    raw = getattr(resp, "content", "").strip()

    def _try_parse_json(s: str) -> dict | None:
        try:
            return json.loads(s)
        except Exception:
            # fallback: estrai il primo blocco {...} per sicurezza
            try:
                start = s.find("{"); end = s.rfind("}")
                if start != -1 and end != -1 and end > start:
                    return json.loads(s[start:end+1])
            except Exception:
                return None
        return None
    updated = _try_parse_json(raw) or prev_report  

    new_messages = list(state["messages"])
    new_messages.append(AIMessage(content="[Reporter] report aggiornato", name="Reporter"))

    print(f"[Reporter] report aggiornato: {json.dumps(updated, ensure_ascii=False)}")

    return {
        "messages": new_messages,
        "shared_report": json.dumps(updated, ensure_ascii=False)
    }
