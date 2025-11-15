from typing_extensions import TypedDict
# from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, AnyMessage # type: ignore
from typing import Annotated
import operator

class SummaryState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    plan: str

def summary_agent(state: SummaryState) -> SummaryState:
    # llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    planning_prompt = [ # type: ignore
        HumanMessage(content="Given the user query, generate a step-by-step plan using available tools."),
        *state["messages"]
    ]
    # response = llm(planning_prompt)
    response = HumanMessage(content="mock response")

    state["plan"] = response.content  # type: ignore
    print(f"[SUMMARY] Final Result: {state.get('result', 'N/A')}") # type: ignore
    return state
