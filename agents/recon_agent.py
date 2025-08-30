from langgraph.prebuilt import create_react_agent
from tools.tools import tools
from .state import AgentState
from prompts import RECON_AGENT_PROMPT
from models import get_model
from langchain_core.messages import AIMessage
def extract_summary(messages) -> str:
    """Estrae contenuto testuale dai messaggi, appiattendo liste e forzando in stringa."""
    parts = []
    def _flatten(msgs):
        for m in msgs:
            if isinstance(m, list):
                _flatten(m)
            elif hasattr(m, "content"):
                parts.append(str(m.content))
            else:
                parts.append(str(m))
    _flatten(messages)
    return "\n".join(parts)


def build_recon_agent():
    """
    Recon Agent come ReAct.
    - Usa i tool (terminal_tool, self_rag_tool, ecc.)
    - Riceve dallo state il `shared_report` (solo per contesto)
    - NON aggiorna lo shared_report (compito del Reporter)
    """
    model = get_model(temperature=0)

    # Core ReAct agent (lavora su messages)
    recon_core = create_react_agent(
        model,
        tools=tools,
        prompt=RECON_AGENT_PROMPT,
    )

    def recon_with_context(state: AgentState) -> AgentState:
        shared_report = state.get("shared_report", "Nessuna informazione precedente.")
        last_msg = state["messages"][-1]

        # Costruisco i messaggi da dare al ReAct agent
        enriched_inputs = {
            "messages": [
                ("system", f"Contesto accumulato:\n{shared_report}"),
                ("user", last_msg.content if hasattr(last_msg, "content") else str(last_msg))
            ]
        }
        enriched_inputs["messages"].extend(state["messages"])

        # Invoco il core ReAct agent
        result = recon_core.invoke(enriched_inputs)
        

        summary = extract_summary(result["messages"])

        recon_msg = AIMessage(content=f"[Reconnaissance]\n{summary}", name="Reconnaissance")
        # Ritorno solo i messaggi generati, senza toccare lo shared_report
        return {
            "messages": recon_msg,
            "shared_report": shared_report
        }

    return recon_with_context
