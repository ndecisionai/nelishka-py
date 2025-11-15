from typing_extensions import TypedDict
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class UnifiedState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    result: int
    documents: list[str]
    tool_outputs: dict # type: ignore
    plan: str