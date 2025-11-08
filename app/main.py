from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware  # Importar CORS
import requests

app = FastAPI()

# 🚀 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen (por ahora)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "josue-model"

@app.get("/")
def home():
    return {"mensaje": "Servidor Ollama + FastAPI activo 🚀"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "")

    payload = {
        "model": MODEL_NAME,
        "prompt": mensaje
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return {"respuesta": result.get("response", "")}
    except Exception as e:
        return {"error": str(e)}


