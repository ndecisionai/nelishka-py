from langgraph.graph import StateGraph, START, END # type: ignore
from agentic.agents.state import UnifiedState
from agentic.node_registry import AGENT_REGISTRY # type: ignore

graph = StateGraph(UnifiedState)

# Add nodes
for name, agent_fn in AGENT_REGISTRY.items(): # type: ignore
    graph.add_node(name, agent_fn) # type: ignore
    
def should_run_planner(state: UnifiedState):
    content = state["messages"][-1].content.lower() # type: ignore
    if "plan" in content:
        return "planner"
    return "summary"

# Define edges
graph.add_edge(START, "retrieval")
graph.add_edge("retrieval", "tool")
graph.add_edge("tool", "arithmetic")
graph.add_edge("arithmetic", "llm")
graph.add_conditional_edges("llm", should_run_planner, ["summary", "planner"])
graph.add_edge("summary", END)
graph.add_edge("planner", END)

# Compile and run
compiled_graph = graph.compile() # type: ignore


# from langgraph.graph import StateGraph, START, END # type: ignore
# from typing_extensions import TypedDict, Annotated
# from langchain.messages import HumanMessage, SystemMessage, AnyMessage, ToolMessage # type: ignore
# import operator

# # -------------------
# # State Definition
# # -------------------
# class AgentState(TypedDict):
#     messages: Annotated[list[AnyMessage], operator.add]
#     result: int

# # -------------------
# # Fixed Node: Log Input
# # -------------------
# def log_input(state: AgentState):
#     last_message = state["messages"][-1]
#     print(f"[LOG] Received message: {last_message.content}") # type: ignore
#     return state  # no change to state

# # -------------------
# # Conditional Node: Arithmetic Agent
# # -------------------
# def arithmetic_agent(state: AgentState):
#     last_message = state["messages"][-1]
#     # Simple parser for "Add X and Y" or "Subtract X and Y"
#     content = last_message.content.lower() # type: ignore
#     if "add" in content:
#         parts = [int(s) for s in content.split() if s.isdigit()] # type: ignore
#         state["result"] = sum(parts)
#     elif "subtract" in content:
#         parts = [int(s) for s in content.split() if s.isdigit()] # type: ignore
#         state["result"] = parts[0] - parts[1]
#     return state

# # -------------------
# # Conditional Node: Threshold Check
# # -------------------
# def threshold_check(state: AgentState):
#     if state.get("result", 0) > 10:
#         print("[INFO] Result exceeds threshold 10")
#     return state

# # -------------------
# # Fixed Node: Summary
# # -------------------
# def summary_node(state: AgentState):
#     print(f"[SUMMARY] Final Result: {state.get('result', 'N/A')}")
#     return state

# # -------------------
# # Conditional edge decision
# # -------------------
# def should_run_arithmetic(state: AgentState):
#     content = state["messages"][-1].content.lower() # type: ignore
#     if "add" in content or "subtract" in content:
#         return "arithmetic_agent"
#     return "summary_node"

# def should_run_threshold(state: AgentState):
#     if state.get("result", 0) > 10:
#         return "threshold_check"
#     return "summary_node"

# # -------------------
# # Build Graph
# # -------------------
# graph = StateGraph(AgentState)

# # Fixed nodes
# graph.add_node("log_input", log_input) # type: ignore
# graph.add_node("summary_node", summary_node) # type: ignore

# # Conditional agentic nodes
# graph.add_node("arithmetic_agent", arithmetic_agent) # type: ignore
# graph.add_node("threshold_check", threshold_check) # type: ignore

# # Edges
# graph.add_edge(START, "log_input")
# graph.add_conditional_edges("log_input", should_run_arithmetic, ["arithmetic_agent", "summary_node"])
# graph.add_conditional_edges("arithmetic_agent", should_run_threshold, ["threshold_check", "summary_node"])
# graph.add_edge("threshold_check", "summary_node")
# graph.add_edge("summary_node", END)

# # -------------------
# # Test Graph
# # -------------------
# messages = [HumanMessage(content="Add 7 and 5")]
# state = {"messages": messages}

# final_state = graph.compile().invoke(state) # type: ignore
