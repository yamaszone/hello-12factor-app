from fastapi import FastAPI
import logging
import os
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

logger.info('Initializing FastAPI...')
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": os.getenv("WORLD")}
