from typing import Dict, TypedDict, Any, List
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
# from langchain.agents import Tool
# from langchain.tools import DuckDuckGoSearchRun
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class RiskAssessmentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    data: Dict[str, Any]
    log: List[str]

def risk_assessment_agent(
    state: RiskAssessmentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> RiskAssessmentState:
    
    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Risk assessment executing: {config.description}")
    
    query = state["messages"][-1].content  # type: ignore

    # search = DuckDuckGoSearchRun()
    # result = search.run(query)
    
    data = state.get("data")
    if data is None:
        data = state.setdefault("data", {"initial_query": "", "retrieved_data": "", "analyst": [], "potential": [], "risk_assessment": []})
        
    data["risk_assessment"].append("risk assessment did some analization stuff")

    print(f"[Risk] Assessment of some risks")  # {result[:100]}...
    return state