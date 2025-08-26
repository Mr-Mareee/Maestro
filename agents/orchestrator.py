from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from prompts import ORCHESTRATOR_PROMPT
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from .state import AgentState

# Orchestrator: unico non ReAct agent
def orchestrator(state: AgentState) -> AgentState:
    """
    Nodo decisionale: sceglie la prossima fase in base al contenuto del shared_report.
    Usa un LLM per analizzare il documento e restituire uno stato tra:
    Reconnaissance, Scanning, Exploitation, PrivilegeEscalation, FinalReporter.
    """
    # Carica il documento condiviso (generato dal Reporter)
    shared_report = state.get("shared_report", "Nessuna informazione precedente.")
    # Prompt di ruolo per l’orchestrator
    system_prompt = SystemMessage(content=(
        ORCHESTRATOR_PROMPT
    ))

    human_prompt = HumanMessage(content=f"Report condiviso:\n{shared_report}")

    # Invochiamo l'LLM
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    response = model.invoke([system_prompt, human_prompt])

    # Puliamo l'output per estrarre lo stato
    decision = response.content.strip()
    print(f"[Orchestrator] LLM output: {decision}")
    if decision not in [
        "Reconnaissance",
        "Scanning",
        "Exploitation",
        "PrivilegeEscalation",
        "FinalReporter"
    ]:
        decision = "Reconnaissance"  # fallback conservativo
    print(f"[Orchestrator] decisione: {decision}")
    return {"messages": [decision]}




def route_from_orchestrator(state: AgentState):
    """
    Router: legge l'ultima decisione e indirizza verso la fase corretta.
    """
    last = state["messages"][-1]
    last = last.content
    if "Reconnaissance" in last:
        return "to_recon"
    elif "Scanning" in last:
        return "to_scan"
    elif "Exploitation" in last:
        return "to_exploit"
    elif "Privilege" in last:
        return "to_priv"
    elif "final_report" in last or "FinalReporter" in last:
        return "to_final_report"
    else:
        return "to_final_report"
