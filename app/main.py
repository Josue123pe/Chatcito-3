from fastapi import FastAPI, Request
import requests

app = FastAPI()

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

