from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class DownloadRequest(BaseModel):
    url: HttpUrl
    
class VideoMetadata(BaseModel):
    title: str
    duration: int  # duración en segundos
    thumbnail: str
    uploader: str
    upload_date: str
    view_count: Optional[int] = None
    description: Optional[str] = None

class DownloadResponse(BaseModel):
    success: bool
    message: str
    metadata: Optional[VideoMetadata] = None
    mp3_url: Optional[str] = None
    download_url: Optional[str] = None  # URL temporal para descargar el MP3
    processed_at: datetime