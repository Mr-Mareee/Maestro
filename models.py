from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

#provider="openai"
provider="anthropic"
def get_model(temperature: float = 0):
    """
    Ritorna un modello LLM in base al provider scelto.
    provider: "openai" | "anthropic"
    model_name: nome del modello (default dipende dal provider)
    """
    if provider == "openai":
        return ChatOpenAI(
            model="gpt-4o",
            temperature=temperature
        )
    elif provider == "anthropic":
        return ChatAnthropic(
            model="claude-sonnet-4-20250514",
            temperature=temperature
        )
    else:
        raise ValueError(f"Provider non supportato: {provider}")
