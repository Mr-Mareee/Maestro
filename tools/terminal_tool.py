import subprocess
import os
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool

class ShellCommandInput(BaseModel):
    """Input schema for shell command execution."""
    command: str = Field(description="Complete shell command to execute. Example: 'nmap -sV -p- 10.10.10.1' or 'whoami'")

def execute_shell_command(command: str) -> str:
    """Execute shell command with enhanced security and logging"""
    if not command.strip():
        return "Error: Empty command provided"
    
    print(f"🔧 Executing: {command}")
    
    try:
        print(" IL COMANDONE è : ", command)
        # Enhanced security: block dangerous commands in production
        dangerous_patterns = ['rm -rf /', 'dd if=', 'mkfs', 'fdisk', ':(){ :|:& };:']
        if any(pattern in command.lower() for pattern in dangerous_patterns):
            return f"⚠️ Potentially dangerous command blocked: {command}"
        
        # Execute with enhanced settings
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=950,  # 15 minutes timeout
            cwd=os.path.expanduser("~"),  # Execute from home directory
            env=dict(os.environ, TERM='xterm-256color')  # Better terminal support
        )
        
        # Enhanced output formatting
        response = f"💻 Command: {command}\n"
        response += f"📊 Exit Code: {result.returncode}\n"
        
        if result.stdout:
            response += f"\n✅ STDOUT:\n{result.stdout}"
        
        if result.stderr:
            response += f"\n⚠️ STDERR:\n{result.stderr}"
        
        if not result.stdout and not result.stderr:
            response += "\n✅ Command completed successfully with no output"
            
        # Add execution time and status
        status = "✅ SUCCESS" if result.returncode == 0 else "❌ FAILED"
        response += f"\n🏁 Status: {status}"
            
        return response
        
    except subprocess.TimeoutExpired:
        return f"⏰ Command timed out after 15 minutes: {command}"
    except Exception as e:
        return f"❌ Error executing command '{command}': {str(e)}"

terminal_tool = StructuredTool.from_function(
    func=execute_shell_command,
    name="terminal_tool",
    description = """Esegue comandi NON INTERATTIVI di shell sul sistema target.
    Usalo per ricognizione, scanning, enumerazione, exploit e privilege escalation applicando, dove possibili, flag di non interattività.
    Costruisci comandi validi e completi (es. 'nmap -sV 10.10.10.1')."""
    ,
    args_schema=ShellCommandInput
)