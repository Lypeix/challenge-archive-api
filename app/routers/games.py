from typing import Annotated # imports Python's ability to attach extra metadata to a type
                             # metadata means data describing other data or behavior

from fastapi import APIRouter, Depends, HTTPException, status # APIRouter groups related endpoints
                                               # Depends tells FastAPI to get a value from another function

from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import GameCreate, GameResponse, GameUpdate

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

@router.get(
    "",
    response_model=list[GameResponse]
)
def list_games(
    session: Annotated[Session, Depends(get_db)]
):
    return crud.get_games(session)

@router.get(
    "/{game_id}"
)
def get_game_id(
    game_id: int,
    session: Annotated[Session, Depends(get_db)]
):
    game = crud.get_game_by_id(session, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return game

@router.patch(
    "/{game_id}",
    response_model=GameResponse
)
def update_game(
    game_id: int,
    game_data: GameUpdate,
    session: Annotated[Session, Depends(get_db)]
):
    game = crud.get_game_by_id(session, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return crud.update_game(session, game, game_data)