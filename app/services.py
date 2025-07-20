from yt_dlp import YoutubeDL
from tempfile import NamedTemporaryFile
import os

def download_audio_stream_from_youtube(url: str):
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file_path = temp_file.name

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_file_path,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return temp_file_path
