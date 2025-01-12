import os
import yt_dlp as youtube_dl

def download_youtube_video(url: str, output_dir="files/audio/") -> str:
    """Downloads a YouTube video as audio and returns the file path."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_config = {
        "format": "bestaudio/best",
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    }

    print(f"Downloading video from {url}...")
    with youtube_dl.YoutubeDL(ydl_config) as ydl:
        ydl.download([url])

    # Find the downloaded file
    files = [f for f in os.listdir(output_dir) if f.endswith(".mp3")]
    return os.path.join(output_dir, files[0])
