from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(
    title="YouTube to MP3 Downloader API",
    description="API para convertir videos de YouTube a MP3 y extraer metadatos",
    version="1.0.0"
)

# Configurar CORS para permitir peticiones desde Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios concretos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar las rutas
app.include_router(router, prefix="/api/v1", tags=["downloads"])

@app.get("/")
async def root():
    return {"message": "YouTube to MP3 Downloader API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)