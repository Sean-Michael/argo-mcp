from contextlib import asynccontextmanager
from argo_mcp.config import Settings
from argo_mcp.telemetry.setup import setup_telemetry

from fastapi import FastAPI

# Import settings from .env
settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_telemetry(app, settings)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
