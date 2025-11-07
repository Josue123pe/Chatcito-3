# Usa Python como base (permite pip)
FROM python:3.10-slim

# Instalar dependencias del sistema y curl para descargar Ollama
RUN apt-get update && apt-get install -y curl && apt-get clean

# Instalar Ollama dentro del contenedor
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copiar el Modelfile
COPY Modelfile /Modelfile

# Crear el modelo personalizado
RUN ollama serve & sleep 5 && ollama create josue-model -f /Modelfile

# Copiar tus archivos de la app
COPY main.py /main.py
COPY requirements.txt /requirements.txt

# Instalar dependencias Python
RUN pip install --no-cache-dir -r /requirements.txt

# Exponer el puerto
EXPOSE 8000

# Ejecutar Ollama y tu app FastAPI juntos
CMD ollama serve & uvicorn main:app --host 0.0.0.0 --port 8000


