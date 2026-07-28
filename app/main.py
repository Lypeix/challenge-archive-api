from fastapi import FastAPI

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Challenge Archive API!",
    description="A nice little personal project where I'll add some gaming challanges",
    lifespan=lifespan
)