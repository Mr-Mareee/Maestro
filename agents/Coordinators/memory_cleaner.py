# agents/memory_cleaner.py
from typing import List
from models import get_model
from langchain_core.messages import SystemMessage,AIMessage, HumanMessage
from ..state import AgentState
from prompts import MEMORY_CLEANER_PROMPT
from langgraph.graph.message import add_messages

import json

def memory_cleaner(state: AgentState) -> AgentState:
    """
    Dopo il Reporter, riassume i messaggi precedenti in un unico blocco.
    Mantiene solo gli ultimi `keep_last` intatti per continuità.
    """
    messages = state.get("messages", [])
    keep_last = 10
    if len(messages) <= keep_last:
        return state

    old_msgs = messages[:-keep_last]
    recent_msgs = messages[-keep_last:]

    # concateno i vecchi messaggi in testo
    old_text = "\n".join(
        f"{m.type.upper()}: {getattr(m, 'content', str(m))}" for m in old_msgs
    )

    # chiamo un LLM per riassumere
    model = get_model(temperature=0)
    system = SystemMessage(
        content=MEMORY_CLEANER_PROMPT
    )
    human = HumanMessage(content=old_text)  # cutoff di sicurezza

    summary = model.invoke([system, human])
    summary_text = getattr(summary, "content", "").strip()

    cleaned_state = dict(state)
    cleaned_state["messages"] = add_messages(AIMessage(content=f"[MemoryCleaner Summary]\n{summary_text}"),recent_msgs)
    print('MEMORY CLEANER')
    print('*'*20)
    print(cleaned_state)
    print('*'*20)
    print('MEMORY CLEANER')

    return cleaned_state
