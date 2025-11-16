from agentic.agent_manager import AgentManager
from agentic.types import AgentState

manager = AgentManager()

agent = manager.get_agent("analyst")

if agent is None:
    raise RuntimeError("Agent not loaded!")

state: AgentState = {
    "data": {},
    "references": {},
    "messages": [],
    "log": []
}

result = agent(state)

print(result)
