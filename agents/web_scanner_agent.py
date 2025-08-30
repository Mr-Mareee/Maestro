from langgraph.prebuilt import create_react_agent
from tools.tools import tools
from .state import AgentState
from prompts import WEB_SCANNER_AGENT_PROMPT
from models import get_model
from langchain_core.messages import AIMessage
def flatten_messages(msgs):
            flat = []
            for m in msgs:
                if isinstance(m, list):
                    flat.extend(flatten_messages(m))
                else:
                    flat.append(m)
            return flat

def build_web_scanner_agent():
    """
    Web Scanner Agent come ReAct.
    - Usa i tool (terminal_tool, self_rag_tool, ecc.)
    - Riceve dallo state il `shared_report` (solo per contesto)
    - NON aggiorna lo shared_report (compito del Reporter)
    """
    model = get_model(temperature=0)

    # Core ReAct agent (lavora su messages)
    web_scanner_core = create_react_agent(
        model,
        tools=tools,
        prompt=WEB_SCANNER_AGENT_PROMPT,
    )

    def web_scanner_with_context(state: AgentState) -> AgentState:
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
        result = web_scanner_core.invoke(enriched_inputs)


        flat_messages = flatten_messages(result["messages"])
        summary = "\n".join(m.content for m in flat_messages if hasattr(m, "content"))

        web_scanner_msg = AIMessage(content=f"[WebScanner]\n{summary}", name="WebScanner")
        # Ritorno solo i messaggi generati, senza toccare lo shared_report
        return {
            "messages": web_scanner_msg,
            "shared_report": shared_report
        }

    return web_scanner_with_context
