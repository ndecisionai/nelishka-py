from langchain_core.messages import HumanMessage
from agentic.graph_builder import compiled_graph

final_state = compiled_graph.invoke({ # type: ignore
	"messages": [HumanMessage(content="Add 3 and 4")],
	"documents": [],
	"tool_outputs": {},
	"plan": "",
})