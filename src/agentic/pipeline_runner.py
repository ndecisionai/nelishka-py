from langchain_core.messages import HumanMessage
from agentic.graph_builder import compiled_graph

final_state = compiled_graph.invoke({ # type: ignore
  "messages": [
    HumanMessage(
      content="Analyze Apple stock (AAPL) for me. Summarize the key points I should know as an investor, including financial, risks, recent performance, and your general outlook."
    )
  ],
 	# TODO - create a decorator/wrapper for automatic data initialization
 	"data": {},
	"documents": [],
	"logs": [],
})

for item in final_state["logs"]:
	print(f"- {item}")