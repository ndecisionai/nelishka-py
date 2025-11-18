from typing import Dict, TypedDict
from agentic.agent_types import AgentState
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
# from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, AnyMessage # type: ignore
from typing import Annotated
import operator

class FeatureStoreState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    plan: str

def feature_store_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:
    
    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Feature store executing: {config.description}")
    
    # llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    planning_prompt = [ # type: ignore
        HumanMessage(content="Given the user query, generate a step-by-step plan using available tools."),
        *state["messages"]
    ]
    # response = llm(planning_prompt)
    response = HumanMessage(content="stored all feature in the database")

    state["plan"] = response.content  # type: ignore
    print(f"[FEATURE] Stored features: {response.content}") # type: ignore
    return state