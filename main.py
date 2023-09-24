# main.py en el directorio principal

from app.main import app as fastapi_app

# Configurar otros aspectos globales si es necesario

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
