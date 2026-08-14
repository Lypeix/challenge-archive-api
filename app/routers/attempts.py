from typing import Annotated

from fastapi import FastAPI, APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app import crud

from app.database import get_db

from app.schemas import AttemptCreate, AttemptResponse, AttemptUpdate


router = APIRouter(
    tags=["Attempts"]
)

@router.post(
    "/challenges/{challenge_id}/attempts",
    response_model=AttemptResponse,
    status_code=status.HTTP_201_CREATED
)

def create_attempt(
    challenge_id: int,
    attempt_data: AttemptCreate,
    session: Annotated[Session, Depends(get_db)]
):

    challenge = crud.get_challenge_by_id(
        session,
        challenge_id
    )


    if challenge is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found"
        )

    return crud.create_attempt(
        session,
        challenge,
        attempt_data
    )