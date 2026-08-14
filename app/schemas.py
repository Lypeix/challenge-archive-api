from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from enum import StrEnum

class GameBase(BaseModel): # defines what client sends to the server when creating a game
    model_config = ConfigDict( # defines how a model is supposed to behave
        str_strip_whitespace=True 
        )

    title: str = Field(
        min_length=1,
        max_length=100
    )

    genre: str = Field(
        min_length=1,
        max_length=50
    )

    release_year: int = Field( # ge = greater or equal, le = lesser or equal (int equivalent of min/max_length)
        ge=1950,
        le=2100
    )

class GameCreate(GameBase): # inherits validation from gamebase
    pass

class GameUpdate(BaseModel): # defines how optional fields for partial game updates
    model_config = ConfigDict( 
        str_strip_whitespace=True 
        )

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    genre: str | None = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    release_year: int | None = Field(
        default=None,
        ge=1950,
        le=2100
    )

class GameResponse(GameBase): # defines what the server returns to the client
    model_config = ConfigDict(
        from_attributes=True, # allows Pydantic to read object attributes n convert them into JSON response schema
    )

    id: int
    created_at: datetime


# CHALLENGE SECTION


class ChallengeStatus(StrEnum): # StrEnum members behave like strings while restricting values to the member values
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class ChallengeDifficulty(StrEnum): 
    HARD = "hard"
    SUPER = "super"
    HYPER = "hyper"
    EXTREME = "extreme"


class ChallengeBase(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    title: str = Field(
        min_length=1,
        max_length=150
    )

    rules: str = Field(
        min_length=1,
        max_length=5000
    )

    status: ChallengeStatus = ChallengeStatus.PLANNED
    difficulty: ChallengeDifficulty


class ChallengeCreate(ChallengeBase): # game_id is absent because it comes from URL
    pass


class ChallengeUpdate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=150
    )

    rules: str | None = Field(
        default=None,
        min_length=1,
        max_length=5000
    )

    status: ChallengeStatus | None = None
    difficulty: ChallengeDifficulty | None = None
    
class ChallengeResponse(ChallengeBase): # must inherit from ChallengeBase, otherwise responses would omit it's contents (title, rules, status, difficulty)
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True
    )

    id: int
    game_id: int 
    created_at: datetime

    
class AttemptResult(StrEnum):
    PROGRESSED = "progressed"    
    COMPLETED = "completed"


class AttemptBase(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    result: AttemptResult

    duration_minutes: int = Field(
        ge=0
    )


    death_count: int = Field(
        default=0,
        ge=0
    )

    notes: str = Field(
        default=None,
        max_length=2000
    )


class AttemptCreate(AttemptBase): # provides clean place for future create-only fields
    pass


class AttemptUpdate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    result: AttemptResult | None = None 

    duration_minutes: int | None = Field(
        ge=0
    )


    death_count: int | None = Field(
        default=0,
        ge=0
    )

    notes: str | None = Field(
        default=None,
        max_length=2000
    )


class AttemptResponse(AttemptBase):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True
    )

    id: int
    challenge_id: int
    created_at: datetime