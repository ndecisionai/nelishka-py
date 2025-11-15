from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, AnyMessage # type: ignore
from agentic.graph_builder import compiled_graph

final_state = compiled_graph.invoke({ # type: ignore
    "messages": [HumanMessage(content="Add 3 and 4")],
    "documents": [],
    "tool_outputs": {},
    "plan": "",
})


# from langchain.tools import tool # type: ignore
# from langchain.chat_models import init_chat_model


# model = init_chat_model(
#     "claude-sonnet-4-5-20250929",
#     temperature=0,
#     api_key=""
# )


# # Define tools
# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return a * b


# @tool
# def add(a: int, b: int) -> int:
#     """Adds `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return a + b


# @tool
# def divide(a: int, b: int) -> float:
#     """Divide `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return a / b


# # Augment the LLM with tools
# tools = [add, multiply, divide]
# tools_by_name = {tool.name: tool for tool in tools}
# model_with_tools = model.bind_tools(tools) # type: ignore

# from langchain.messages import AnyMessage
# from typing_extensions import TypedDict, Annotated
# import operator


# class MessagesState(TypedDict):
#     messages: Annotated[list[AnyMessage], operator.add]
#     llm_calls: int
    
# from langchain.messages import SystemMessage


# def llm_call(state: dict): # type: ignore
#     """LLM decides whether to call a tool or not"""

#     return {
#         "messages": [
#             model_with_tools.invoke(
#                 [
#                     SystemMessage(
#                         content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
#                     )
#                 ]
#                 + state["messages"] # type: ignore
#             )
#         ],
#         "llm_calls": state.get('llm_calls', 0) + 1 # type: ignore
#     } # type: ignore
    
# from langchain.messages import ToolMessage


# def tool_node(state: dict): # type: ignore
#     """Performs the tool call"""

#     result = []
#     for tool_call in state["messages"][-1].tool_calls: # type: ignore
#         tool = tools_by_name[tool_call["name"]]
#         observation = tool.invoke(tool_call["args"]) # type: ignore
#         result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"])) # type: ignore
#     return {"messages": result} # type: ignore
  
# from typing import Literal
# from langgraph.graph import StateGraph, START, END # type: ignore


# def should_continue(state: MessagesState) -> Literal["tool_node", END]: # type: ignore
#     """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

#     messages = state["messages"]
#     last_message = messages[-1]

#     # If the LLM makes a tool call, then perform an action
#     if last_message.tool_calls: # type: ignore
#         return "tool_node"

#     # Otherwise, we stop (reply to the user)
#     return END
  
# # Build workflow
# agent_builder = StateGraph(MessagesState)

# # Add nodes
# agent_builder.add_node("llm_call", llm_call) # type: ignore
# agent_builder.add_node("tool_node", tool_node) # type: ignore

# # Add edges to connect nodes
# agent_builder.add_edge(START, "llm_call")
# agent_builder.add_conditional_edges(
#     "llm_call",
#     should_continue, # type: ignore
#     ["tool_node", END]
# )
# agent_builder.add_edge("tool_node", "llm_call")

# # Compile the agent
# agent = agent_builder.compile() # type: ignore

# # Show the agent
# from IPython.display import Image, display # type: ignore
# display(Image(agent.get_graph(xray=True).draw_mermaid_png())) # type: ignore

# # Invoke
# from langchain.messages import HumanMessage
# messages = [HumanMessage(content="Add 3 and 4.")]
# messages = agent.invoke({"messages": messages}) # type: ignore
# for m in messages["messages"]:
#     m.pretty_print()
    
