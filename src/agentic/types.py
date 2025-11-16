from typing import TypedDict, List, Any, Optional, Dict
from langchain_core.messages import BaseMessage
from typing_extensions import Annotated
import operator


class AgentState(TypedDict, total=False):
    messages: Annotated[List[BaseMessage], operator.add]
    data: Dict[str, Any]
    references: Dict[str, Any]
    context: Optional[Any]
    log: List[str]
