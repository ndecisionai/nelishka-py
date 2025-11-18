from typing import Dict, TypedDict
from agentic.agent_types import AgentState
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
# from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, AnyMessage # type: ignore
from typing import Annotated
import operator
import random

class TraderState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    result: str

def trader_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:
    
    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Feature store executing: {config.description}")
    
    # llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    messages = state["messages"] # type: ignore
    # response = llm(messages)
    
    response = HumanMessage(content="Final result based on all analses")

    state["messages"].append(response) # type: ignore
    print(f"[TRADER] Response: {response.content}") # type: ignore
    return state