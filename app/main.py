from fastapi import FastAPI, Request
import subprocess, json

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "")

    # Ejecutar ollama desde el contenedor
    proceso = subprocess.run(
        ["ollama", "run", "josue-model"],
        input=mensaje.encode(),
        capture_output=True
    )

    respuesta = proceso.stdout.decode()
    return {"respuesta": respuesta}
