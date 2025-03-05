from fastapi import FastAPI, Form
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from loguru import logger
import os
import psutil
from starlette.responses import Response

app = FastAPI()

# Configuration des métriques Prometheus
messages_counter = Counter("messages_total", "Nombre total de messages reçus", ["choice"])
cpu_usage = Gauge("cpu_usage", "Utilisation du CPU")
memory_usage = Gauge("memory_usage", "Utilisation de la mémoire")

def log_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}

@app.post("/data")
async def receive_data(data: str = Form(...)):
    logger.info(f"Received data: {data}")
    messages_counter.labels(choice=data).inc()
    log_metrics()
    return {"message": f"Data {data} received"}

@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
