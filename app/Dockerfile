# Imagen base con Ollama
FROM ollama/ollama

# Copiar tu modelo
COPY Modelfile /Modelfile

# Crear el modelo
RUN ollama create josue-model -f /Modelfile

# Instalar dependencias para FastAPI
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install fastapi uvicorn

# Copiar el archivo principal
COPY main.py /main.py

# Exponer el puerto
EXPOSE 8000

# Ejecutar el servidor
CMD ollama serve & uvicorn main:app --host 0.0.0.0 --port 8000