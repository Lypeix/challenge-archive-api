# py -m uvicorn app.main:app --reload

from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.database import engine
from app.routers import games, challenges, attempts

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield # app handles requests when paused here
    finally:
        engine.dispose() # closes engine's connections when the app is finished handling requests


app = FastAPI(
    title="Challenge Archive API!",
    description="A nice little personal project where I'll add some gaming challenges",
    lifespan=lifespan
)

app.include_router(games.router)
app.include_router(challenges.router)
app.include_router(attempts.router)