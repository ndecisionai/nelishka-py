from typing import Dict

from agentic.agent_protocol import AgentCallable
from agentic.agent_manager import AgentManager

manager = AgentManager()

agents_list = manager.list_agents()

AGENT_REGISTRY: Dict[str, AgentCallable] = {
	name: agent
	for name in agents_list
	if (agent := manager.get_agent(name)) is not None
}