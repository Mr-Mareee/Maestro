from langchain_core.tools import tool
from .terminal_tool import terminal_tool
from .self_rag.self_rag_tool import self_rag_tool

@tool
def retriever_tool(query:str) -> str:
    """
    un tool che cerca e ritorna informazioni rilevanti dal database
    """

    docs = retriever.invoke(query) 
    if not docs:
        return "nessun documento rilevante trovato." 
    results = []
    for i,doc in enumerate(docs):
        results.append(f"Documento {i+1}:\n{doc.page_content}\n")

    return "\n".join(results)


@tool
def add(a: int, b:int):
    """This is an addition function that adds 2 numbers together"""

    return a + b 

@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b

tools = [terminal_tool,self_rag_tool]
