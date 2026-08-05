from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class Game(BaseModel): # BaseModel is a parent class that makes the Game class inherit all of Pydantic's functionality
    model_config = ConfigDict( # ConfigDict customizes how this model validates data
                               # things inside ConfigDict() parantheses control the behavior of the whole Game model
        str_strip_whitespace=True
    ) 

