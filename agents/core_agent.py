from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv  
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from .recon_agent import build_recon_agent
from .orchestrator import orchestrator, route_from_orchestrator
from .reporter_agent import reporter_agent
from .final_reporter import final_reporter
from .scanning_agent import build_scanning_agent
from .exploitation_agent import build_exploit_agent
from .privesc_agent import build_privesc_agent
from .state import AgentState
load_dotenv()

graph = StateGraph(AgentState)

graph.add_node("Orchestrator", orchestrator)
graph.add_node("Reconnaissance", build_recon_agent() )
graph.add_node("Scanning", build_scanning_agent())
graph.add_node("Exploitation", build_exploit_agent())
graph.add_node("PrivilegeEscalation", build_privesc_agent())
graph.add_node("Reporter", reporter_agent)
graph.add_node("FinalReporter", final_reporter)

graph.set_entry_point("Reporter")

graph.add_conditional_edges(
    "Orchestrator",
    route_from_orchestrator,
    {
        "to_recon": "Reconnaissance",
        "to_scan": "Scanning",
        "to_exploit": "Exploitation",
        "to_priv": "PrivilegeEscalation",
        "to_final_report": "FinalReporter",
    },
)

graph.add_edge("Reconnaissance", "Reporter")
graph.add_edge("Scanning", "Reporter")
graph.add_edge("Exploitation", "Reporter")
graph.add_edge("PrivilegeEscalation", "Reporter")

graph.add_edge("Reporter", "Orchestrator")

graph.add_edge("FinalReporter", END)

app = graph.compile()

ip = "10.10.11.69"
extra_infos = "As is common in real life Windows pentests, you will start the Fluffy box with credentials for the following account: j.fleischman / J0elTHEM4n1990!"
prompt_iniziale = f"IP: {ip}\n{extra_infos}"

# --- Test veloce ---
if __name__ == "__main__":
    inputs = {"messages": [("user", prompt_iniziale )]}
    for step in app.stream(inputs, stream_mode="values"):
        node = step.get("__node__") or step.get("__step__") or step.get('name') or "UnknownNode"
        msg = step["messages"][-1]
        content = msg.content if hasattr(msg, "content") else str(msg)
        print(f"[{node}] {content}")
