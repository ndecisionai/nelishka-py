from rich.console import Console
from rich.tree import Tree
from rich.padding import Padding

console = Console()

def main(graph_name: str = "default"):
    console.rule(f"[bold blue]Graph: {graph_name}[/bold blue]")
    
    description_text = (
        f"The agent [bold cyan]{graph_name}[/bold cyan] is about to execute its workflow.\n"
        "It will load data, process features, and run its reasoning steps.\n"
        "Please wait..."
    )
    console.print(Padding(description_text, (0, 0, 1, 0)))
    
    tree = Tree("Agentic Graph")
    node_a = tree.add("Data Loader")
    node_b = tree.add("Embedding Generator")
    node_c = tree.add("Reasoning Agent")
    node_a.add("Preprocessing")
    node_b.add("Vector Store")
    node_c.add("LLM Node")
    console.print(Padding(tree, (0, 0, 1, 0)))
