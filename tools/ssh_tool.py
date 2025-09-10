import paramiko  # type: ignore
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage


class SSH_CommandInput(BaseModel):
    """Input schema for SSH command execution."""
    command: str = Field(description="Complete shell command to execute on the remote machine")
    username: str = Field(description="SSH username for the remote machine")
    password: str = Field(description="SSH password for the remote machine")
    hostname: str = Field(description="Hostname or IP address of the remote machine")
    port: int = Field(default=22, description="SSH port of the remote machine, default is 22")


def connected_kali(command, username, password, hostname, port=22) -> str:
    ssh_client=paramiko.SSHClient()
    print('*'*20)
    print(f"\n[Esecuzione comando: {command} con  SSH su {hostname}:{port} come {username}]")
    print('*'*20)
    ans = input("Procedo? (y/n): ")
    if ans.lower() != 'y':
           return "Comando SSH annullato dall'utente."
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

    ssh_client.connect(hostname=hostname, port=port, username=username, password=password)

    try:
         stdin, stdout, stderr=ssh_client.exec_command(command)

         output=stdout.read().decode()

         error=stderr.read().decode()
         answer = ""
         if output:
              answer = output
         if error:
              answer = error
         if answer:
                 print(f"[Output del comando SSH]:\n{answer}\n")
                 return answer
         return BaseMessage(content="Nessun output restituito.")
    finally:
         ssh_client.close()

ssh_tool = StructuredTool.from_function(
    func=connected_kali,
    name="ssh_tool",
    description = """Esegue comandi NON INTERATTIVI di ssh sul sistema target.""",
    args_schema=SSH_CommandInput
)
