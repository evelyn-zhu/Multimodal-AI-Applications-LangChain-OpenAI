import openai
import os

def transcribe_audio(audio_file: str) -> str:
    """Transcribes an audio file using Whisper API."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    with open(audio_file, "rb") as audio:
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=audio
        )
    return response["text"]
