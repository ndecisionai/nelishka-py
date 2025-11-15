from typing_extensions import TypedDict
# from langchain.agents import Tool
# from langchain.tools import DuckDuckGoSearchRun
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class ToolState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    tool_outputs: dict # type: ignore

def tool_agent(state: ToolState) -> ToolState:
    query = state["messages"][-1].content  # type: ignore

    # search = DuckDuckGoSearchRun()
    # result = search.run(query)
    
    result = ["A", "B", "C", "D"]

    state["tool_outputs"] = {"search_result": result}
    print(f"[TOOL] Search result: {result[:100]}...")
    return state