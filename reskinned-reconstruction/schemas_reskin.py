from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class GameBase(BaseModel): # BaseModel is a parent class that makes the Game class inherit all of Pydantic's functionality
    model_config = ConfigDict( # ConfigDict customizes how this model validates data
                               # things inside ConfigDict() parantheses control the behavior of the whole Game model
        str_strip_whitespace=True
    )

    title: str = Field(
        max_length=100,
        min_length=1
    )

    genre: str = Field(
        max_length=150,
        min_length=1
    )

    release_date: int = Field(
        ge=1950,
        le=2100
    )

class GameCreate(GameBase): # creates a new Pydantic model that inherits everything from the GameBase model
    pass # basically empty placeholder cause class requires at least one statement

class GameUpdate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    title: str | None = Field(
        default=None, # makes this field optional, ommited values default to None... basically you don't have to type anything 
        max_length=100,
        min_length=1
    )

    genre: str | None = Field(
        default=None,
        max_length=150,
        min_length=1
    )

    release_date: int | None = Field(
        default=None,
        ge=1950,
        le=2100
    )

