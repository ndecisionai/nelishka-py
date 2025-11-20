from langgraph.graph import StateGraph, START, END # type: ignore
from agentic.agent_types import AgentState
from agentic.node_registry import AGENT_REGISTRY

graph = StateGraph(AgentState)

for name, agent_fn in AGENT_REGISTRY.items():
	graph.add_node(name, agent_fn) # type: ignore
 
	
def should_discuss_more(state: AgentState):
	content = state["messages"][-1].content.lower() # type: ignore
 
	if "risk_evaluator" in content:
		return "risk_evaluator"
	return "trader"

graph.add_edge(START, "data_loader")
graph.add_edge("data_loader", "analyst")
graph.add_edge("analyst", "potential_field_evaluator")
graph.add_conditional_edges(
  "potential_field_evaluator", 
  should_discuss_more, 
  ["risk_evaluator", "trader"]
)
graph.add_edge("risk_evaluator", "potential_field_evaluator")
graph.add_edge("trader", "feature_store")
graph.add_edge("feature_store", END)

compiled_graph = graph.compile() # type: ignore