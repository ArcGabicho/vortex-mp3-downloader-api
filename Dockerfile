FROM python:3.11-slim

WORKDIR /app

# Instalar FFmpeg y dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Verificar que FFmpeg está instalado correctamente
RUN ffmpeg -version

# Exponer el puerto (Railway maneja esto automáticamente)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]