from langchain_core.tools import tool
from .terminal_tool import terminal_tool
from .self_rag.self_rag_tool import self_rag_tool
from .human_tool import human_tool
from langchain_community.tools.shell.tool import ShellTool

shell_tool = ShellTool(description="Esegue comandi shell non interattivi  sul sistema operativo. Usalo con cautela.",ask_human_input=True)
tools = [shell_tool,self_rag_tool,human_tool]
