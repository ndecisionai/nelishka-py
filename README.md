# Agentic Workflow Framework

A modular, configuration-driven framework for building and executing **LangGraph-based agent workflows**. Define agents, tools, and workflows entirely via YAML — no code changes required.

## Key Features

- **Agentic Graph Execution** using [LangGraph](https://github.com/langchain-ai/langgraph)
- **Dynamic loading** of agents, tools, and workflows from YAML configs
- **CLI interface** for running agents, invoking workflows, and visualizing graphs
- **Extensible architecture**: plug in new agents/tools without modifying core logic

## Core Concepts

| Component  | Description |
|------------|-------------|
| **Tools**  | Stateless, atomic operations (e.g., fetch prices, run inference). Configured in `configs/tools/`, implemented in `src/agentic/tools/`. |
| **Agents** | Reasoning nodes with optional LLMs and tool access. Configured in `configs/agents/`, implemented in `src/agentic/agents/`. |
| **Workflows** | Directed graphs of agents defining execution flow. Configured in `configs/graphs/`, built via `graph_builder.py`. |

## Project Structure

```
configs/         # YAML configs for agents, tools, workflows
src/
  agentic/       # Core runtime: agents, tools, graph builder
  cli/           # CLI commands (run, list, visualize)
tests/           # Unit tests
```

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/ndecisionai/nelishka-py.git
cd nelishka-py
pip install -e .
```

## CLI Usage

```bash
nelishka-cli
```

## Testing

Run unit and integration tests:

```bash
pytest tests/
```

## Contributing

**All contributions are welcome — feel free to open issues, suggest improvements, or submit pull requests!**
