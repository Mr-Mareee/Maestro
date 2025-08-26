# agents/scanning_agent.py
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.tools import tools
from .state import AgentState
from prompts import SCANNING_AGENT_PROMPT
from langchain_core.messages import AIMessage

def build_scanning_agent():
    """
    Scanning Agent come ReAct.
    - Analizza servizi già scoperti
    - Usa tool (es. nmap -sV, searchsploit, ecc.)
    - NON aggiorna lo shared_report (compito del Reporter)
    """
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    scanning_core = create_react_agent(
        model,
        tools=tools,
        prompt=SCANNING_AGENT_PROMPT,
    )

    def scanning_with_context(state: AgentState) -> AgentState:
        shared_report = state.get("shared_report", "Nessuna informazione precedente.")
        last_msg = state["messages"][-1]

        enriched_inputs = {
            "messages": [
                ("system", f"Contesto accumulato:\n{shared_report}"),
                ("user", last_msg.content if hasattr(last_msg, "content") else str(last_msg))
            ]
        }

        result = scanning_core.invoke(enriched_inputs)
        summary = "\n".join(m.content for m in result["messages"] if hasattr(m, "content"))
        scanning_msg = AIMessage(content=f"[Scanning]\n{summary}", name="Scanning")

        return {
            "messages": scanning_msg,
            "shared_report": shared_report
        }

    return scanning_with_context
