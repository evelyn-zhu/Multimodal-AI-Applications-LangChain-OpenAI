import os
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
# Safely store your key as an env var
os.environ["OPENAI_API_KEY"] = "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"

# Now OpenAIEmbeddings will automatically find it
from langchain.embeddings.openai import OpenAIEmbeddings
def setup_qa(docs):
    """Sets up the QA system using LangChain."""
    db = DocArrayInMemorySearch.from_documents(
        docs, OpenAIEmbeddings(openai_api_key="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")
    )
    retriever = db.as_retriever()
    llm = ChatOpenAI(temperature=0.0)
    qa_system = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        verbose=True,
    )
    return qa_system