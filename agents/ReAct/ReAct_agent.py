from langgraph.prebuilt import create_react_agent
from tools.tools import tools
from ..state import AgentState
from prompts import prompts_agent
from models import get_model
from langchain_core.messages import AIMessage
from langgraph.graph.message import add_messages

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


def build_react_agent(name):
    """
    ReAct agent.
    - Usa i tool (terminal_tool, self_rag_tool, ecc.)
    - Legge lo shared_report come contesto
    - Produce UN SOLO messaggio finale e lo aggiunge allo storico
    - NON aggiorna lo shared_report (compito del Reporter)
    """
    model = get_model(temperature=0)  # o get_model()

    recon_core = create_react_agent(
        model,
        tools=tools[name],
        prompt=prompts_agent[name],
    )

    def agent_with_context(state: AgentState) -> AgentState:
        shared_report = state.get("shared_report", "Nessuna informazione precedente.")
        #messages = state.get('messages','')
        # Prepara input per il ReAct agent
        enriched_inputs = {
            "messages": [
                ("user", f"Contesto attuale:\n{shared_report}\n\nProcedi con la tua fase.")
            ]
        }

        # Invoca il core ReAct agent
        result = recon_core.invoke(enriched_inputs)

        # Estrai il riassunto finale (es. dalla tua funzione extract_summary)
        summary = result['messages'][-1].content if result['messages'] else "Nessun output generato."

        # Crea il messaggio finale dell'agente
        agent_considerations = AIMessage(
            content=f"[{name}]\n{summary}",
            name=name
        )

        new_state = dict(state)
        new_state["messages"] = add_messages(state["messages"], agent_considerations)
        new_state["shared_report"] = shared_report

        return new_state

    return agent_with_context