from typing import TypedDict, Dict, Annotated, Any, List
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
from langchain.messages import AnyMessage
import operator

class AnalystState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    data: Dict[str, Any]
    log: List[str]


def analyst_agent(
    state: AnalystState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AnalystState:

    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Analyst executing: {config.description}")

    if "context_pack" in tools:
        state["context"] = tools["context_pack"](
            symbol=state.get("data.symbol", {}),
        )
    
    data = state.get("data")
    if data is None:
        data = state.setdefault("data", {"initial_query": "", "retrieved_data": "", "analyst": [], "potential": [], "risk_assessment": []})
        
    data["analyst"].append("analyst did some analyse stuff")
        
    print(f"[ANALYST] Done")

    return state
