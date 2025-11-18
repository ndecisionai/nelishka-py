from typing import Dict, TypedDict
from agentic.agent_types import AgentState
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
from langchain.messages import AnyMessage, HumanMessage
from typing import Annotated
import operator

class PotentialState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    result: int

def potential_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:
    
    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Potential executing: {config.description}")
    
    content = state["messages"][-1].content.lower() # type: ignore
    
    data = state.get("data")
    if data is None:
        data = state.setdefault("data", {"initial_query": "", "retrieved_data": "", "analyst": [], "potential": [], "risk_assessment": []})
        
    data["potential"].append("potential did some analization stuff")
    
    if len(data["risk_assessment"]) < 2:
        state["messages"].append(HumanMessage(content="it's better to assess some risks using risk_assessment"))
    else:
        state["messages"].append(HumanMessage(content="lets move forward to trader agent to see the final result"))
        
    print(f"[POTENTIAL] Response: {state["messages"][-1].content.lower()}") # type: ignore
    return state