from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import ChallengeCreate, ChallengeResponse

router = APIRouter(
    tags=["Challenges"]
)

@router.post(
    "/games/{game_id}/challenges",
    response_model=ChallengeResponse,
    status_code=status.HTTP_201_CREATED
)

def challenge_create(
    game_id: int,
    challenge_data: ChallengeCreate,
    session: Annotated[Session, Depends(get_db)]
):
    game = crud.get_game_by_id(session, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return crud.create_challenge(session, game, challenge_data)
    