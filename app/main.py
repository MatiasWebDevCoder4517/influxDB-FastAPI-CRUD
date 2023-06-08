from fastapi import FastAPI
from logging.config import dictConfig
from app.src.config.logger import LogConfig

dictConfig(LogConfig().dict())
app = FastAPI()

@app.get("/influxCRUD")
def app_influxDB():
    return {"status": "OK"}