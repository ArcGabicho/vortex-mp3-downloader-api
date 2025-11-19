#!/bin/bash
set -e

echo "🚀 Starting Vortex MP3 Downloader API..."
echo "📍 Port: ${PORT:-8000}"
echo "📁 Working directory: $(pwd)"
echo "🐍 Python version: $(python --version)"

# Create temp directory if it doesn't exist
mkdir -p temp

# Start the application with proper logging
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port ${PORT:-8000} \
    --workers 1 \
    --log-level info \
    --access-log