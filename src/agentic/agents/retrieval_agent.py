from typing_extensions import TypedDict
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.schema import Document
from langchain.messages import AnyMessage
from typing import Annotated
import operator

class RetrievalState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    documents: list[str]

def retrieval_agent(state: RetrievalState) -> RetrievalState:
    query = state["messages"][-1].content  # type: ignore

    # vectorstore = FAISS.load_local("vectorstore_index", OpenAIEmbeddings())
    # docs: list[Document] = vectorstore.similarity_search(query, k=3)

    # state["documents"] = [doc.page_content for doc in docs]
    # print(f"[RETRIEVAL] Retrieved {len(docs)} documents.")
    print(f"[RETRIEVAL] Retrieved")
    return state