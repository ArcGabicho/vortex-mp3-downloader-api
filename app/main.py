from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware  # <-- Importa el middleware
from pydantic import BaseModel
from app.services import download_audio_stream_from_youtube
import os

app = FastAPI()

# Agrega configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vortex-mp3-downloader-app.vercel.app"],  # Puedes poner el dominio de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
