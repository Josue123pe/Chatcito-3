# Imagen base con Ollama
FROM ollama/ollama

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install fastapi uvicorn

# Exponer puerto
EXPOSE 8000

# Iniciar Ollama, crear el modelo (una vez iniciado el servidor) y luego lanzar FastAPI
CMD ollama serve & sleep 5 && ollama create josue-model -f /app/Modelfile && uvicorn main:app --host 0.0.0.0 --port 8000

