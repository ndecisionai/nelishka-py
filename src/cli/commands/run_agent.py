from rich.console import Console
from rich.progress import track
from rich.padding import Padding
import time

console = Console()

def main(agent: str = "default"):
    console.rule(f"[bold magenta]Running Agent: {agent}[/bold magenta]")
    
    description_text = (
        f"The agent [bold cyan]{agent}[/bold cyan] is about to execute its workflow.\n"
        "It will load data, process features, and run its reasoning steps.\n\n"
        "Please wait..."
    )
    console.print(Padding(description_text, (0, 0, 1, 0)))
    
    for _ in track(range(8), description=f"Running {agent} "):
        time.sleep(1)

    console.print(Padding(f"[green]{agent}[/green] completed successfully!", (0, 0, 1, 0)))
