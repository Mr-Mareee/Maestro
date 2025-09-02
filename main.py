from dotenv import load_dotenv  

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END


from agents.Coordinators.orchestrator import orchestrator, route_from_orchestrator
from agents.Coordinators.reporter_agent import reporter_agent
from agents.Coordinators.final_reporter import final_reporter
from agents.Coordinators.memory_cleaner import memory_cleaner

from agents.state import AgentState

import time

from agents.ReAct.ReAct_agent import build_react_agent


load_dotenv()

agents = ['Reconnaissance', 'PrivilegeEscalation', 'WebScanner']

graph = StateGraph(AgentState)

graph.add_node("Orchestrator", orchestrator)
graph.add_node("Reporter", reporter_agent)
graph.add_node("FinalReporter", final_reporter)
graph.add_node("MemoryCleaner", memory_cleaner)

graph.set_entry_point("Reporter")

for agent in agents:
    graph.add_node(agent, build_react_agent(agent)) 




graph.add_conditional_edges(
    "Orchestrator",
    route_from_orchestrator,
    {
        "to_recon": "Reconnaissance",
        #"to_scan": "Scanning",
        #"to_exploit": "Exploitation",
        "to_priv": "PrivilegeEscalation",
        "to_web_scan": "WebScanner",
        "to_final_report": "FinalReporter",
    },
)
for agent in agents:
    graph.add_edge(agent, "Reporter")


graph.add_edge("Reporter", "MemoryCleaner")
graph.add_edge("MemoryCleaner","Orchestrator")

graph.add_edge("FinalReporter", END)

app = graph.compile()


#se devo testare in locale
#ip='127.0.0.1'

ip = "127.0.0.1"
extra_infos = ""
prompt_iniziale = f"IP: {ip}\n{extra_infos}. ora inizio: {time.ctime()}"

# --- Test veloce ---
if __name__ == "__main__":
    inputs = {"messages": [HumanMessage(content=prompt_iniziale,name="User")]}
    for step in app.stream(inputs, stream_mode="values", max_iterations=50):
        node = step.get("__node__") or step.get("__step__") or step.get('name') or "UnknownNode"
        msg = step["messages"][-1]
        content = msg.content if hasattr(msg, "content") else str(msg)
        print(f"[{node}] {content}")
