from typing import Dict
from src.agentic.types import AgentState
from src.agentic.config_models import AgentConfig
from src.agentic.tool_protocol import ToolCallable


def analyst_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:

    log = state.setdefault("log", [])
    log.append(f"Analyst executing: {config.description}")

    if "llm_context_pack" in tools:
        state["context"] = tools["llm_context_pack"](
            data=state.get("data", {}),
            references=state.get("references", {})
        )

    return state
