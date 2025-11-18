from langgraph.graph import StateGraph, START, END
from agentic.unified_state import UnifiedState
from agentic.node_registry import AGENT_REGISTRY

graph = StateGraph(UnifiedState)

for name, agent_fn in AGENT_REGISTRY.items():
	graph.add_node(name, agent_fn)
 
	
def should_discuss_more(state: UnifiedState):
	content = state["messages"][-1].content.lower()
	if "risk_assessment" in content:
		return "risk_assessment"
	return "trader"

graph.add_edge(START, "data_loader")
graph.add_edge("data_loader", "analyst")
graph.add_edge("analyst", "potential")
graph.add_conditional_edges(
  "potential", 
  should_discuss_more, 
  ["risk_assessment", "trader"]
)
graph.add_edge("risk_assessment", "potential")
graph.add_edge("trader", "feature_store")
graph.add_edge("feature_store", END)

compiled_graph = graph.compile()