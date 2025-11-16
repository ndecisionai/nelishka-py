from typing import Protocol
from .types import AgentState


class AgentCallable(Protocol):
    def __call__(
        self,
        state: AgentState,
    ) -> AgentState:
        ...
