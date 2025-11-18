from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime
import os
import tempfile
from urllib.parse import unquote, quote
from app.models.schemas import DownloadRequest, DownloadResponse, VideoMetadata
from app.services.downloader import YoutubeDownloader

router = APIRouter()

@router.post("/download-mp3", response_model=DownloadResponse)
async def download_mp3(request: DownloadRequest):
    """
    Descarga un video de YouTube, lo convierte a MP3 y devuelve los metadatos
    junto con una URL temporal para descargar el archivo.
    """
    try:
        downloader = YoutubeDownloader()
        
        # Obtener metadatos del video
        video_info = await downloader.get_video_info(str(request.url))
        
        # Descargar y convertir a MP3
        mp3_path = await downloader.download_as_mp3(str(request.url))
        
        # Crear metadatos del video
        metadata = VideoMetadata(
            title=video_info.get('title', 'Unknown'),
            duration=video_info.get('duration', 0),
            thumbnail=video_info.get('thumbnail', ''),
            uploader=video_info.get('uploader', 'Unknown'),
            upload_date=video_info.get('upload_date', ''),
            view_count=video_info.get('view_count'),
            description=video_info.get('description')
        )
        
        # Crear URL temporal para descargar el archivo
        filename = os.path.basename(mp3_path)
        # Codificar el nombre del archivo para la URL
        encoded_filename = quote(filename)
        download_url = f"/api/v1/files/{encoded_filename}"
        
        return DownloadResponse(
            success=True,
            message="Video procesado exitosamente",
            metadata=metadata,
            mp3_url=mp3_path,
            download_url=download_url,
            processed_at=datetime.now()
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error procesando el video: {str(e)}")

@router.get("/files/{filename}")
async def download_file(filename: str):
    """
    Endpoint para descargar el archivo MP3 procesado.
    """
    # Decodificar el nombre del archivo (convierte %20 en espacios, etc.)
    decoded_filename = unquote(filename)
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, decoded_filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Archivo no encontrado: {decoded_filename}")
    
    return FileResponse(
        path=file_path,
        filename=decoded_filename,
        media_type="audio/mpeg"
    )

@router.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "ok", "timestamp": datetime.now()}