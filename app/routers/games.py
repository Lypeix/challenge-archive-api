from typing import Annotated # imports Python's ability to attach extra metadata to a type
                             # metadata means data describing other data or behavior

from fastapi import APIRouter, Depends, status # APIRouter groups related endpoints
                                               # Depends tells FastAPI to get a value from another function

from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import GameCreate, GameResponse

router = APIRouter( # creates a router that groups game-related endpoints
    prefix="/games", # automatically places /games before every path made by this router, eg. "" in router.post means "/games"
    tags=["Games"] # visually groups these endpoints under the Games section in SwaggerUI 
) 

@router.post( # registers function below as HTTP endpoint
    "",
    response_model=GameResponse, # successful output must match GameResponse from schemas.py
    status_code=status.HTTP_201_CREATED 

)

def create_game(
    game_data: GameCreate, # GameCreate is a Pydantic model, so FastAPI treats it as a JSON request body
    session: Annotated[Session, Depends(get_db)] # tells Python, VSC n type checkers that session is a SQLAlchemy
):                                               # gets the value for session parameter through get_db
                                                 # FastAPI is responsible for calling get_db, so no need to add parantheses at the end
    return crud.create_game( # calls create_game n its parameters from crud
        session,
        game_data
    )