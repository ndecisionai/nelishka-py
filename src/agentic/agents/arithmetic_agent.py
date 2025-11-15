from typing_extensions import TypedDict
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class ArithmeticState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    result: int

def arithmetic_agent(state: ArithmeticState) -> ArithmeticState:
    content = state["messages"][-1].content.lower() # type: ignore
    parts = [int(s) for s in content.split() if s.isdigit()] # type: ignore
    if "add" in content:
        state["result"] = sum(parts)
    elif "subtract" in content:
        state["result"] = parts[0] - parts[1]
        
    print(f"[ARITH] Response: {content}") # type: ignore
    return state