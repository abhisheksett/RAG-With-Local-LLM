from langchain_community.vectorstores import DocArrayInMemorySearch
from model_setup import get_embedding

# Global variable
vectorstore = None

def store_in_vector_db(documents):
    global vectorstore
    vectorstore = DocArrayInMemorySearch.from_documents(
        documents,
        embedding=get_embedding(),
    )
    # retriever = vectorstore.as_retriever()
    # print(retriever.invoke("How Search Works?"))

def get_vectorstore():
    global vectorstore
    if vectorstore is None:
        raise ValueError("Vector store has not been initialized. Call store_in_vector_db first.")
    return vectorstore

def retrieve_from_vector_db(question, k=5):
    results = retriever.retrieve(question, k=k)
    return results