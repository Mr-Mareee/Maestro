import os
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from langchain_core.messages import HumanMessage
class HumanCommandInput(BaseModel):
    """Input schema for asking human intervention."""
    command: str = Field(description="Comando o consiglio richiesto dall'agente.")

def ask_human_intervention(command: str) -> str:
    """
    Quando l'agnete ha dubbi, invoca questo tool.
    fa una domanda all'utente umano e attende la risposta.
    """
    print("\n[Human Intervention Requested]")
    print(f"🤖 L'agente suggerisce / chiede: {command}")
    print("💡 Inserisci una risposta (può essere un consiglio, un comando alternativo o 'approvato'): ")
    
    try:
        human_reply = input("👉 La tua risposta: ")
    except EOFError:
        human_reply = "No input provided."
    human_reply = HumanMessage(content='[Human reply]'+ human_reply)

    return human_reply

human_tool = StructuredTool.from_function(
    func=ask_human_intervention,
    name="human_tool",
    description="Strumento per chiedere intervento umano quando l'agente ha dubbi su un comando o una decisione.",
    args_schema=HumanCommandInput
)
