from typing import Dict, TypedDict
from agentic.agent_types import AgentState
from agentic.config_models import AgentConfig
from agentic.tool_protocol import ToolCallable
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.schema import Document
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class DataLoaderState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    documents: list[str]

def data_loader_agent(
    state: AgentState,
    config: AgentConfig,
    tools: Dict[str, ToolCallable]
) -> AgentState:
    
    log = state.get("log")
    if log is None:
        log = state.setdefault("log", [])
    log.append(f"Data loader executing: {config.description}")
    
    query = state["messages"][-1].content

    # vectorstore = FAISS.load_local("vectorstore_index", OpenAIEmbeddings())
    # docs: list[Document] = vectorstore.similarity_search(query, k=3)

    # state["documents"] = [doc.page_content for doc in docs]
    # print(f"[DATA] Retrieved {len(docs)} documents.")
    
    data = state.get("data")
    if data is None:
        data = state.setdefault("data", {"initial_query": "", "retrieved_data": "", "analyst": [], "potential": [], "risk_assessment": []})
        
    data["initial_query"] = query
    data["retrieved_data"] = "fetched some raw data from remote"
    
    print(f"[DATA] Loaded data")
    return state