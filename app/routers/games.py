from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import GameCreate, GameResponse

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)

@router.post(
    "",
    response_model=GameResponse,
    status_code=status.HTTP_201_CREATED

)

def create_game(
    game_data: GameCreate,
    session: Annotated[Session, Depends(get_db)]
):
    return crud.create_game(
        session,
        game_data
    )