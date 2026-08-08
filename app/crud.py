from sqlalchemy.orm import Session 

from sqlalchemy import select 

from app.models import Game
from app.schemas import GameCreate, GameUpdate

def create_game(
    session: Session,
    game_data: GameCreate
) -> Game:
    game = Game(
        **game_data.model_dump()
    )

    session.add(game)
    session.commit()
    session.refresh(game)

    return game

def get_games(
    session: Session
) -> list[Game]:
    statement = ( # the variable that stores db instructions below
        select(Game) # select basically means get/read
        .order_by(Game.id)
    )

    games = session.scalars(statement).all() # executes the statement n gives all selected game ORM objects
                                             # without scalars, SQLAlchemy would return a row containing selected value instead of value itself, 
                                             # so I'd have to extract the value from row wrappers
    return list(games)

def get_game_by_id(
    session: Session,
    game_id: int
) -> Game | None:
    return session.get(Game, game_id)

def update_game(
    session: Session,
    game: Game,
    game_data: GameUpdate
) -> Game:

    update_data = game_data.model_dump(
        exclude_unset=True, # includes only fields actually sent by the client
        exclude_none=True   # prevents null values from replacing current database values
    )

    for field_name, new_value in update_data.items():
        setattr(game, field_name, new_value) # dynamic way of typing eg. game.title = new_value

    # game was already loaded previously in this session, so no need to track it again using session.add(game)

    session.commit() 
    session.refresh(game)

    return game