from sqlalchemy.orm import Session

from app.models import Game
from app.schemas import GameCreate

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