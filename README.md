# 🎵 YouTube to MP3 Downloader API

![Portada](https://i.imgur.com/mU8Uxu2.png)

Una API REST moderna construida con **FastAPI** para descargar videos de YouTube y convertirlos a MP3, extrayendo metadatos completos del video. 

## 🚀 Características

- ✅ Descarga y conversión automática de YouTube a MP3
- ✅ Extracción completa de metadatos (título, duración, thumbnail, etc.)
- ✅ API REST documentada automáticamente con Swagger/OpenAPI
- ✅ Soporte para CORS (listo para frontends)
- ✅ Manejo asíncrono para mejor rendimiento
- ✅ URLs temporales para descarga de archivos
- ✅ Codificación correcta de nombres de archivo

## 📋 Requisitos

- Python 3.8+
- FFmpeg (para conversión de audio)
- yt-dlp
- FastAPI y dependencias

### Instalar FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Arch Linux:**
```bash
sudo pacman -S ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Descargar desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/ArcGabicho/vortex-mp3-downloader-api.git
cd vortex-mp3-downloader-api
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: http://localhost:8000

## 📚 Documentación de la API

### Endpoints Disponibles

#### 🔗 URLs Base
- **Desarrollo:** `http://localhost:8000`
- **Documentación:** `http://localhost:8000/docs`
- **Esquema OpenAPI:** `http://localhost:8000/openapi.json`

#### 📝 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Mensaje de bienvenida |
| `POST` | `/api/v1/download-mp3` | Descargar y convertir video a MP3 |
| `GET` | `/api/v1/files/{filename}` | Descargar archivo MP3 generado |
| `GET` | `/api/v1/health` | Estado de la API |

### 🎬 POST /api/v1/download-mp3

Descarga un video de YouTube, lo convierte a MP3 y devuelve metadatos completos.

#### Request Body
```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

#### Response
```json
{
  "success": true,
  "message": "Video procesado exitosamente",
  "metadata": {
    "title": "Never Gonna Give You Up",
    "duration": 213,
    "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
    "uploader": "Rick Astley",
    "upload_date": "20091025",
    "view_count": 1234567890,
    "description": "The official video for Rick Astley..."
  },
  "mp3_url": "/tmp/Never Gonna Give You Up.mp3",
  "download_url": "/api/v1/files/Never%20Gonna%20Give%20You%20Up.mp3",
  "processed_at": "2025-11-18T22:38:03.171059"
}
```

### 📥 GET /api/v1/files/{filename}

Descarga el archivo MP3 procesado usando la URL temporal proporcionada.

#### Ejemplo
```bash
GET /api/v1/files/Never%20Gonna%20Give%20You%20Up.mp3
```

## 🧪 Cómo Probar la API

### 1. Usando la documentación interactiva (Recomendado)
1. Ve a http://localhost:8000/docs
2. Busca `POST /api/v1/download-mp3`
3. Haz clic en "Try it out"
4. Ingresa una URL de YouTube
5. Ejecuta y descarga el MP3 usando la URL devuelta

### 2. Usando cURL
```bash
# Paso 1: Procesar video
curl -X POST "http://localhost:8000/api/v1/download-mp3" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'

# Paso 2: Descargar MP3 (usar download_url de la respuesta anterior)
curl -O "http://localhost:8000/api/v1/files/Never%20Gonna%20Give%20You%20Up.mp3"
```

### 3. Usando JavaScript (Frontend)
```javascript
// Procesar video
const response = await fetch('http://localhost:8000/api/v1/download-mp3', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' })
});

const data = await response.json();

// Descargar MP3
if (data.success) {
  const link = document.createElement('a');
  link.href = `http://localhost:8000${data.download_url}`;
  link.download = `${data.metadata.title}.mp3`;
  link.click();
  
  // Guardar metadatos en Firestore (tu código aquí)
  saveToFirestore(data.metadata);
}
```

## 🏗️ Estructura del Proyecto

```
vortex-mp3-downloader-api/
├── app/
│   ├── main.py              # Punto de entrada de FastAPI
│   ├── api/
│   │   └── routes.py        # Definición de endpoints
│   ├── models/
│   │   └── schemas.py       # Modelos Pydantic
│   └── services/
│       └── downloader.py    # Lógica de descarga con yt-dlp
├── requirements.txt         # Dependencias Python
├── README.md               # Este archivo
└── .gitignore             # Archivos ignorados por Git
```

## 🐳 Docker (Opcional)

```dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## ⚠️ Consideraciones Importantes

- Los archivos MP3 se almacenan temporalmente en `/tmp/`
- La API no persiste historial (diseñado para frontends)
- Configura `allow_origins` en producción para mayor seguridad
- Considera implementar rate limiting en producción
- FFmpeg es requerido para la conversión de audio

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).