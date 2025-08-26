from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Dict

class SelfRAGInput(BaseModel):
    query: str = Field(description="Query da proporre al retriever.")
    shared_report: str = Field(description="Report condiviso con lo stato dell'agente.")
    agent_role: str = Field(description="Ruolo dell'agente che invoca (es: Reconnaissance, Scanning, Exploitation, PrivEsc).")


# Input schema
def self_rag_retrieve(query: str, shared_report: str, agent_role: str) -> Dict[str, str]:
    """
    Finto Self-RAG multi-KB:
    - in base all'agente che invoca, consulta la sua knowledge base simulata
    - restituisce un comando e reasoning
    """
    context = f"{agent_role}\n{query}\n{shared_report}"
    print('-'*20)
    print("Context per Self-RAG:", context)
    print('-'*20)
    if agent_role == "Reconnaissance":
        if "80" in context or "http" in context.lower():
            return {
                "command": "whatweb http://target",
                "reasoning": "Recon: trovato HTTP, uso whatweb per tecnologie web."
            }
        else:
            return {
                "command": "nmap -sT -p- --min-rate 5005 target",
                "reasoning": "Recon: eseguo scansione full-port per enumerare servizi."
            }

    elif agent_role == "Scanning":
        if "445" in context or "smb" in context.lower():
            return {
                "command": "enum4linux target",
                "reasoning": "Scanning: trovato SMB, uso enum4linux per analizzare condivisioni e utenti."
            }
        else:
            return {
                "command": "nmap -sV -p 22,80 --min-rate=5000 target",
                "reasoning": "Scanning: eseguo version detection sui servizi principali."
            }

    elif agent_role == "Exploitation":
        return {
            "command": "searchsploit apache 2.4.18",
            "reasoning": "Exploitation: trovato Apache 2.4.18, cerco exploit noti con searchsploit."
        }

    elif agent_role == "PrivilegeEscalation":
        return {
            "command": "sudo -l",
            "reasoning": "PrivEsc: controllo i privilegi sudo dell'utente compromesso."
        }

    else:
        return {
            "command": "echo 'Nessuna azione definita'",
            "reasoning": "Agente sconosciuto o non supportato."
        }
# Tool
self_rag_tool = StructuredTool.from_function(
    func=self_rag_retrieve,
    name="self_rag_tool",
    description="🔍 SELF-RAG TOOL - Suggerisce comandi utili per la fase di reconnaissance.",
    args_schema=SelfRAGInput
)
