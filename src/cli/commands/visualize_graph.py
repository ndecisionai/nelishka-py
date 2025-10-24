"""
Nelishka CLI — Visualize Graph
==============================

This module implements the `visualize-graph` command for the Nelishka Interactive CLI.
It provides a rich, tree-based visualization of an agentic workflow graph, allowing
users to quickly understand the structure of a pipeline or process.

The visualization is purely console-based and uses the `rich` library to render
a hierarchical tree representing the components and their relationships.

Features:
---------
- Displays a styled header with the name of the graph being visualized.
- Prints a short description of the graph’s purpose and workflow.
- Renders a hierarchical Rich tree illustrating the key components (agents, tools, etc.).
- Uses colorized and padded formatting for readability.

Usage:
------
From the Nelishka interactive console:

    λ visualize-graph my_workflow

Or run directly as a Python module:

    $ python -m cli.commands.visualize_graph

Example Output:
---------------
────────────────────────────── Graph: my_workflow ───────────────────────────────
The agent my_workflow is about to execute its workflow.
It will load data, process features, and run its reasoning steps.
Please wait...

Agentic Graph
├── Data Loader
│   └── Preprocessing
├── Embedding Generator
│   └── Vector Store
└── Reasoning Agent
    └── LLM Node

Dependencies:
-------------
- rich

"""

from rich.console import Console
from rich.tree import Tree
from rich.padding import Padding

console = Console()


def main(graph_name: str = "default") -> None:
    """
    Visualize a predefined graph or workflow structure in a Rich tree format.

    Parameters
    ----------
    graph_name : str, optional
        The name of the graph to visualize. Defaults to "default".

    Behavior
    --------
    - Displays a console header with the graph name.
    - Prints a short description of the workflow.
    - Renders a static hierarchical tree to illustrate the graph structure.
      (This can be extended in the future to render real workflow configurations.)

    Example
    -------
    >>> main("data_pipeline")
    Displays a Rich-styled tree showing nodes like loaders, agents, and processors.
    """
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
