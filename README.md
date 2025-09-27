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


## � Uso con Docker

Construir la imagen y ejecutar el contenedor:

```bash
docker build -t vortex-mp3-downloader-api .
```

```bash
docker run -d -p 8000:8000 --name vortex-mp3-downloader-api vortex-mp3-downloader-api
```

El servicio estará disponible en `http://localhost:8000`.

Si usas Railway u otra plataforma, el contenedor detectará automáticamente el puerto asignado por la variable de entorno `PORT`.


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
└── LICENSE.md
```

---

## 📦 .env.example

```bash
PORT=8000
```

```bash
TEMP_FOLDER=./temp
```

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).