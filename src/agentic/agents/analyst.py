from typing import Dict
from agentic.agent_types import AgentState
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable


def analyst_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:

    log = state.setdefault("log", [])
    log.append(f"Analyst executing: {config.description}")

    if "context_pack" in tools:
        state["context"] = tools["context_pack"](
            symbol=state.get("data.symbol", {}),
        )

    return state
