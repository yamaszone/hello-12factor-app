from fastapi import FastAPI
from logger import configure_logger

logger = configure_logger()

logger.info('Initializing FastAPI...')
app = FastAPI()

@app.get("/hello")
def say_hello(name: str = "anonymous"):
    return { "Hello" : name + "!" }

@app.get("/healthz")
def healthz():
    return { "status": { "code" : 200, "message": "OK" } }
