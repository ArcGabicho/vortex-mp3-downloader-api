FROM python:3.11-slim

WORKDIR /app

# Instalar FFmpeg y dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear directorio para archivos temporales
RUN mkdir -p /tmp/downloads

# Verificar que FFmpeg está instalado correctamente
RUN ffmpeg -version

# Health check para Railway
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8000}/api/v1/health || exit 1

# Comando para ejecutar la aplicación
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]