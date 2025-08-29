# agents/memory_cleaner.py
from typing import List
from models import get_model
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from .state import AgentState
from prompts import MEMORY_CLEANER_PROMPT
import json

def memory_cleaner(state: AgentState) -> AgentState:
    """
    Dopo il Reporter, riassume i messaggi precedenti in un unico blocco.
    Mantiene solo gli ultimi `keep_last` intatti per continuità.
    """
    messages = state.get("messages", [])
    keep_last = 3
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
    human = HumanMessage(content=old_text[:6000])  # cutoff di sicurezza

    summary = model.invoke([system, human])
    summary_text = getattr(summary, "content", "").strip()

    cleaned_state = dict(state)
    cleaned_state["messages"] = [
        SystemMessage(content=f"[MemoryCleaner Summary]\n{summary_text}")
    ] + recent_msgs

    print('[MemoryCleaner] questi sono i nuovi messaggi'+json.dumps(cleaned_state["messages"], indent=2, ensure_ascii=False))
    return cleaned_state
