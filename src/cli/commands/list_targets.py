from pathlib import Path
from typing import Dict, Any, List
from rich.console import Console
from rich.table import Table
from rich.padding import Padding
from utils.config_loader import load_config, ConfigType, make_config_path

console = Console()

def main() -> None:
    """
    Print all agents, tools, and graphs with name, type, and short description in a table.
    Uses the existing config loader from src.utils.config_loader.
    """
    table = Table(title="")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Type", style="green")
    table.add_column("Description", style="magenta")

    # Helper to load all configs in a folder
    def load_configs(config_type: ConfigType) -> List[Dict[str, Any]]:
        folder_path = make_config_path(config_type)
        folder = folder_path.parent if folder_path.suffix else folder_path  # ensure folder path
        if not folder.exists():
            return []
        configs: List[Dict[str, Any]] = []
        for file_path in folder.glob("*.yml"):
            data = load_config(file_path)
            configs.append(data)
        return configs

    # List agents
    for agent_config in load_configs(ConfigType.AGENT):
        agent_data: Dict[str, Any] = agent_config.get("agent", {})
        if agent_data:
            table.add_row(
                agent_data.get("name", "Unknown"),
                "Agent",
                (agent_data.get("description") or "").split("\n")[0][:70] + "..."
            )

    # List tools
    for tool_config in load_configs(ConfigType.TOOL):
        tool_data: Dict[str, Any] = tool_config.get("tool", {})
        name = tool_data.get("name", "Unknown")
        description = (tool_data.get("description") or "").split("\n")[0][:70]  + "..."
        table.add_row(name, "Tool", description)

    # List graphs
    for graph_config in load_configs(ConfigType.GRAPH):
        name = graph_config.get("name", "Unknown")
        description = (graph_config.get("description") or "").split("\n")[0][:70]  + "..."
        table.add_row(name, "Graph", description)

    console.rule(f"[bold cyan]Available Components[/bold cyan]")
    console.print(Padding(table, (1, 0, 1, 0)))
