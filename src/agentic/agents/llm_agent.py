from typing_extensions import TypedDict
# from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, AnyMessage # type: ignore
from typing import Annotated
import operator
import random

class LLMState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    result: str

def llm_agent(state: LLMState) -> LLMState:
    # llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    messages = state["messages"] # type: ignore
    # response = llm(messages)
    
    response_list = ["create a plan", "something else"]
    response = HumanMessage(content=response_list[random.randint(0, 1)])

    state["messages"].append(response) # type: ignore
    state["result"] = response.content  # type: ignore
    print(f"[LLM] Response: {response.content}") # type: ignore
    return state