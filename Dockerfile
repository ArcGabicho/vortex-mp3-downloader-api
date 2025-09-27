FROM python:3.11-alpine

WORKDIR /app

# Instalar ffmpeg y dependencias necesarias
RUN apk update && \
    apk add --no-cache ffmpeg libsm libxext

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ffmpeg -version && ffprobe -version

# Usa el puerto proporcionado por Railway
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]