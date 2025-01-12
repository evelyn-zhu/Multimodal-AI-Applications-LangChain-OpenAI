from langchain.embeddings.openai import OpenAIEmbeddings
import os
def process_embeddings(text: str):
    """Generates embeddings for given text."""
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    return embeddings.embed_query(text)
