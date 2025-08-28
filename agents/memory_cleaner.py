# agents/memory_cleaner.py
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from prompts import MEMORY_CLEANER_PROMPT
def memory_cleaner(messages: List[BaseMessage], keep_last: int = 3) -> List[BaseMessage]:
    """
    Dopo il Reporter, riassume i messaggi precedenti in un unico blocco.
    Mantiene solo gli ultimi `keep_last` intatti per continuità.
    """
    if len(messages) <= keep_last:
        return messages

    old_msgs = messages[:-keep_last]
    recent_msgs = messages[-keep_last:]

    # concateno i vecchi messaggi in testo
    old_text = "\n".join(
        f"{m.type.upper()}: {getattr(m, 'content', str(m))}" for m in old_msgs
    )

    # chiamo un LLM per riassumere
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    system = SystemMessage(
        content=MEMORY_CLEANER_PROMPT
    )
    human = HumanMessage(content=old_text[:6000])  # cutoff di sicurezza

    summary = model.invoke([system, human])
    summary_text = getattr(summary, "content", "").strip()

    # ricostruisco la nuova lista: summary + recenti
    cleaned = [SystemMessage(content=f"[MemoryCleaner Summary]\n{summary_text}")]
    cleaned.extend(recent_msgs)

    print(f"[MemoryCleaner] Riassunti {len(old_msgs)} messaggi in un summary compatto.")
    return cleaned
