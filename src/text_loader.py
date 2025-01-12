from langchain.document_loaders import TextLoader

def load_transcript(filepath: str):
    """Loads the transcript file into LangChain's document format."""
    loader = TextLoader(filepath)
    docs = loader.load()
    return docs
