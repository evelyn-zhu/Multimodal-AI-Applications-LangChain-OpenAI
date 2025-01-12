from src.download_video import download_youtube_video
from src.transcribe_audio import transcribe_audio
from src.my_embeddings import process_embeddings
from src.text_loader import TextLoader  # Ensure this is correctly imported
from src.qa_system import setup_qa
import os

import openai

# Set your OpenAI API key
openai.api_key = "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"

def main():
    # Step 1: Download YouTube video
    youtube_url = "https://www.youtube.com/watch?v=aqzxYofJ_ck"
    audio_path = download_youtube_video(youtube_url)

    # Step 2: Transcribe the audio
    transcript = transcribe_audio(audio_path)

    # Step 3: Save transcript to file
    transcript_path = "files/transcripts/transcript.txt"
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)  # Ensure directory exists
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"Transcript saved at: {transcript_path}")

    # Step 4: Process embeddings
    processed_data = process_embeddings(transcript)
    print("Processed data:", processed_data)

    # Step 5: Load the transcript and create `docs`
    loader = TextLoader(transcript_path)
    docs = loader.load()
    print(f"Loaded {len(docs)} document(s)")

    # Step 6: Setup QA system
    qa_system = setup_qa(docs)

    # Step 7: Run queries
    queries = [
        "What is this tutorial about?",
        "What is the difference between a training set and test set?",
    ]
    for query in queries:
        response = qa_system.run(query)
        print(f"Query: {query}\nResponse: {response}\n")

if __name__ == "__main__":
    main()
