from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.services import download_audio_stream_from_youtube
import os

app = FastAPI()

class DownloadRequest(BaseModel):
    video_url: str

@app.post("/download-mp3")
async def download_mp3(request: DownloadRequest):
    try:
        file_path = download_audio_stream_from_youtube(request.video_url)
        return FileResponse(
            path=file_path,
            media_type="audio/mpeg",
            filename=os.path.basename(file_path),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
