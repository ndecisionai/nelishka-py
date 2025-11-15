from agentic.agents.arithmetic_agent import arithmetic_agent
from agentic.agents.retrieval_agent import retrieval_agent
from agentic.agents.tool_agent import tool_agent
from agentic.agents.llm_agent import llm_agent
from agentic.agents.planner_agent import planner_agent
from agentic.agents.summary_agent import summary_agent

AGENT_REGISTRY = { # type: ignore
    "arithmetic": arithmetic_agent,
    "retrieval": retrieval_agent,
    "tool": tool_agent,
    "llm": llm_agent,
    "planner": planner_agent,
    "summary": summary_agent,
}