from langchain import OpenAI
from langchain_openai import OpenAIEmbeddings

def test_openai_integration():
    print("Testing OpenAI integration...")
    llm = OpenAI(model_name="text-davinci-003")
    result = llm("What is 2 + 2?")
    print(f"Result: {result}")

def test_embeddings():
    print("Testing embeddings...")
    embeddings = OpenAIEmbeddings(openai_api_key="your-api-key-here")
    vector = embeddings.embed_query("Hello world!")
    print(f"Vector: {vector[:5]}...")

if __name__ == "__main__":
    test_openai_integration()
    test_embeddings()
