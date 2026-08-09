from typing import Annotated # imports Python's ability to attach extra metadata to a type
                             # metadata means data describing other data or behavior

from fastapi import APIRouter, Depends, Query, HTTPException, status # APIRouter groups related endpoints
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
    session: Annotated[Session, Depends(get_db)],
    title: Annotated[str | None, Query(min_length=1, max_length=100)] = None,
    genre: Annotated[str | None, Query(min_length=1, max_length=50)] = None,
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20
):
    return crud.get_games(session, title=title, genre=genre, offset=offset, limit=limit)

@router.get(
    "/{game_id}",
    response_model=GameResponse
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
    game = crud.get_game_by_id(session, game_id) # lets user pick the game id against which this action is supposed to be taken

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return crud.update_game(session, game, game_data)

@router.delete(
    "/{game_id}",
    status_code=status.HTTP_204_NO_CONTENT
)

def delete_game(
    game_id: int,
    session: Annotated[Session, Depends(get_db)]
) -> None:

    game = crud.get_game_by_id(session, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    crud.delete_game(session, game)