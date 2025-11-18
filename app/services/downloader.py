import os
import tempfile
import yt_dlp
from typing import Dict, Any
import asyncio
from concurrent.futures import ThreadPoolExecutor

class YoutubeDownloader:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
        
    async def get_video_info(self, url: str) -> Dict[str, Any]:
        """
        Extrae información del video sin descargarlo.
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        def _extract_info():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        
        # Ejecutar en un hilo separado para no bloquear el loop de eventos
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            info = await loop.run_in_executor(executor, _extract_info)
            
        return info
    
    async def download_as_mp3(self, url: str) -> str:
        """
        Descarga el video y lo convierte a MP3.
        Retorna la ruta del archivo MP3 generado.
        """
        # Configuración para yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.temp_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }
        
        def _download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                # El archivo MP3 ya fue generado por yt-dlp, ahora encontrarlo
                title = info.get('title', 'audio')
                # Limpiar caracteres especiales del título (igual que en outtmpl)
                safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                mp3_filename = f"{safe_title}.mp3"
                mp3_path = os.path.join(self.temp_dir, mp3_filename)
                
                # Verificar que el archivo existe
                if os.path.exists(mp3_path):
                    return mp3_path
                else:
                    # Buscar archivos MP3 en el directorio temporal que empiecen con el título
                    for file in os.listdir(self.temp_dir):
                        if file.endswith('.mp3') and safe_title.split()[0] in file:
                            return os.path.join(self.temp_dir, file)
                    raise Exception(f"No se encontró el archivo MP3 generado: {mp3_filename}")
        
        # Ejecutar en un hilo separado
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            mp3_path = await loop.run_in_executor(executor, _download)
            
        return mp3_path
    
    def cleanup_file(self, file_path: str):
        """
        Elimina un archivo temporal.
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error eliminando archivo {file_path}: {e}")