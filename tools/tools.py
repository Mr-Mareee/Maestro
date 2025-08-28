from langchain_core.tools import tool
from .terminal_tool import terminal_tool
from .self_rag.self_rag_tool import self_rag_tool
from .human_tool import human_tool



tools = [terminal_tool,self_rag_tool,human_tool]
