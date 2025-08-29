# agents/final_reporter.py
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from .state import AgentState
from prompts import FINAL_REPORTER_PROMPT

def final_reporter(state: AgentState) -> AgentState:
    """
    Nodo finale del grafo:
    - Legge lo shared_report (JSON con tutte le info raccolte)
    - Invoca un LLM per generare un report finale in linguaggio naturale
    - Salva il report su file .txt
    - Restituisce un messaggio finale per chiudere il grafo
    """
    model = ChatOpenAI(model="gpt-5", temperature=0)

    shared_report = state.get("shared_report", "{}")
    try:
        report_data = json.loads(shared_report)
    except Exception:
        report_data = {"error": "Report non valido"}

    # Prompt rigido
    system = SystemMessage(content=FINAL_REPORTER_PROMPT)

    human = HumanMessage(content=f"Report JSON:\n{json.dumps(report_data, indent=2, ensure_ascii=False)}")

    response = model.invoke([system, human])
    final_text = response.content.strip()
    # Salva su file
    with open("final_report.txt", "w") as f:
        f.write(final_text)

    # Restituisci un messaggio chiaro e stoppa
    return {
        "messages": [AIMessage(content="[FinalReporter] Report finale generato")],
        "shared_report": shared_report
    }
