from models import get_model
from langgraph.prebuilt import create_react_agent
from tools.tools import tools
from .state import AgentState
from prompts import PRIVESC_AGENT_PROMPT
from langchain_core.messages import AIMessage

def build_privesc_agent():
    """
    Privilege Escalation Agent come ReAct.
    - Usa i tool (terminal_tool, self_rag_tool, ecc.)
    - Riceve dallo state il `shared_report` (solo per contesto)
    - NON aggiorna lo shared_report (compito del Reporter)
    """
    model = get_model(temperature=0)

    privesc_core = create_react_agent(
        model,
        tools=tools,
        prompt=PRIVESC_AGENT_PROMPT,
    )

    def privesc_with_context(state: AgentState) -> AgentState:
        shared_report = state.get("shared_report", "Nessuna informazione precedente.")
        last_msg = state["messages"][-1]

        enriched_inputs = {
            "messages": [
                ("system", f"Contesto accumulato:\n{shared_report}"),
                ("user", last_msg.content if hasattr(last_msg, "content") else str(last_msg))
            ]
        }
        enriched_inputs["messages"].extend(state["messages"])
        result = privesc_core.invoke(enriched_inputs)
        summary = "\n".join(m.content for m in result["messages"] if hasattr(m, "content"))
        privesc_msg = AIMessage(content=f"[Privilege Escalation]\n{summary}", name="PrivilegeEscalation")

        return {
            "messages": privesc_msg,
            "shared_report": shared_report
        }

    return privesc_with_context
