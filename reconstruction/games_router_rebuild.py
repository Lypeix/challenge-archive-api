from typing import Annotated

from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app import crud

from app.database import get_db

from app.schemas import GameCreate, GameResponse

router = APIRouter(
    prefix="/games", # adds /games in the url of every endpoint grouped by this router
    tags=["Games"] # visually groups these endpoints under Games section in SwaggerUI
)

@router.post(
    "",
    response_model=GameResponse,
    status_code=status.HTTP_201_CREATED
)

def create_game(
    game_data: GameCreate, # due to GameCreate being a pydantic model, FastAPI treats game_data as a JSON body
    session: Annotated[Session, Depends(get_db)] # the parameter will contain a SQLAlchemy session
                                                 # FastAPI must gain access to this session through get_db()
):

    return crud.create_game( # calls create_game n its parameters from crud
        game_data,
        session
    )