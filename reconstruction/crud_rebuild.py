from sqlalchemy.orm import Session # session is an object a program uses to interact with the db

from app.models import Game

from app.schemas import GameCreate

def create_game(
    session: Session,
    game_data: GameCreate
) -> Game: # means this function is expected to return Game model
    game = Game( # turns validated request data into a ORM object
        
        **game_data.model_dump() # model_dump turns game_data into a python dict
    )                            # ** unpacks eg. title: x into title=x, as expected by the Game constructor
                                 
    session.add(game) # tells the Session object to track the game object
    session.commit() # saves pending changes made in the current transaction
    session.refresh(game) # updates the python object with db-generated values 

    return game