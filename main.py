import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI

from nacos import init_nacos
from settings import Settings, get_settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_nacos()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    logger.error(settings)
    return {
        "message": "Hello World",
        "settings": settings,
    }


@app.get("/hello/{key}")
async def say_hello(key: str, settings: Settings = Depends(get_settings)):
    return {"message": f"Hello {getattr(settings, key)}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
