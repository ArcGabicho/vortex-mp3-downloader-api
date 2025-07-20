# API Descargar de Videos de Youtube como MP3 con FastAPI

<p align="center">
  <img src="https://i.imgur.com/mU8Uxu2.png" alt="YouTube to MP3 API" width="600"/>
</p>

Una API sencilla hecha con FastAPI para convertir videos de YouTube a archivos MP3.

---

## 🚀 Deploy en Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/ArcGabicho/vortex-mp3-downloader-api)

---

## 📦 Endpoints

### `POST /download-mp3`

Convierte un video de YouTube en MP3.

#### 🧾 Request:
```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

#### 📥 Response:

Descarga directa del archivo .mp3.

---

🧪 Ejemplo de uso con curl

```bash
curl -X POST http://localhost:8000/download-mp3 \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}' \
  --output output.mp3
```

---

## 🛠 Requisitos locales

- Python 3.10+

- ffmpeg (para pydub)

## Instalar dependencias:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

---

## 🐳 Docker

Construir y ejecutar con Docker:

```bash
docker build -t vortex-mp3-downloader-api .
```

```bash
uvicorn app.main:app --reload
```

---

## 📁 Estructura del Proyecto

```
vortex-mp3-downloader-api/
├── app/
│   ├── main.py
│   ├── services.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── .env.example
```

---

## 📦 .env.example

```bash
# Puerto de la aplicación
PORT=8000
```

```bash
# Carpeta temporal de archivos
TEMP_FOLDER=./temp
```

---

## 🧠 Autor

**Gabriel Polack**  
Consultor TI & Arquitecto de Sofware   
📎 [LinkedIn](https://linkedin.com/in/gabriel-polack-castillo/)  
💻 [GitHub](https://github.com/ArcGabicho)

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).