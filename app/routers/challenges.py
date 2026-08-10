from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import ChallengeCreate, ChallengeDifficulty, ChallengeStatus, ChallengeResponse

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

@router.get(
    "/games/{game_id}/challenges",
    response_model=list[ChallengeResponse]
)

def list_challenges(
    game_id: int,
    session: Annotated[Session, Depends(get_db)],
    challenge_status: ChallengeStatus | None = Query(
        default=None,
        alias="status"
    ),
    challenge_difficulty: ChallengeDifficulty | None = Query(
        default=None,
        alias="difficulty"
    )
):
    game = crud.get_game_by_id(session, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return crud.list_challenges(
        session, 
        game, 
        status=challenge_status, 
        difficulty=challenge_difficulty
        )