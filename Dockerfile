FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache ffmpeg libsm libxext

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ffmpeg -version && ffprobe -version

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]