from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

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

class GameUpdate(BaseModel):
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

class GameResponse(GameBase):
    model_config = ConfigDict(
        from_attributes=True, # allows validation from ORM object attributes
        str_strip_whitespace=True
    )

    id: int
    created_at: datetime