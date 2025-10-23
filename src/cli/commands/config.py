from rich.console import Console
from rich.table import Table
from rich.padding import Padding
import yaml
from pathlib import Path

console = Console()
CONFIG_PATH = Path("config.yml")

def show():
    if not CONFIG_PATH.exists():
        console.print("[red]config.yml not found.[/red]")
        return

    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    table = Table(title="")
    table.add_column("Key", style="bold cyan")
    table.add_column("Value", style="green")

    for section, values in config.items():
        table.add_row(f"[bold]{section}[/bold]", "")
        for k, v in values.items():
            table.add_row(f"  {k}", str(v))

    console.rule(f"[bold cyan]Graph: Nelishka Configuration[/bold cyan]")
    console.print(Padding(table, (1, 0, 1, 0)))
