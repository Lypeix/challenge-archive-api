from sqlalchemy.orm import Session 

from sqlalchemy import select 

from app.models import Game, Challenge
from app.schemas import GameCreate, GameUpdate, ChallengeCreate, ChallengeUpdate


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
    session: Session,
    title: str | None = None,
    genre: str | None = None,
    offset: int = 0,
    limit: int = 20

) -> list[Game]:

    statement = ( # the variable that stores db instructions below
        select(Game) # select basically means get/read
        .order_by(Game.id)
        .offset(offset)
        .limit(limit)
    )

    if title is not None:
        statement = statement.where(
            Game.title.ilike(f"%{title}%")
        )

    if genre is not None:
        statement = statement.where(
            Game.genre.ilike(f"%{genre}%")
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


def delete_game(
    session: Session,
    game: Game
) -> None:
    session.delete(game)
    session.commit()


def create_challenge(
    session: Session,
    game: Game,
    challenge_data: ChallengeCreate
) -> Challenge:
    challenge = Challenge(
        game=game, # assigns the relationship, SQLAlchemy gets the parent id n fills challenge.game_id when saving
        **challenge_data.model_dump(mode="json")
    )

    session.add(challenge) 
    session.commit()
    session.refresh(challenge)

    return challenge

def list_challenges(
    session: Session,
    game: Game,
    status: str | None = None,
    difficulty: str | None = None,
    offset: int = 0,
    limit: int = 10
) -> list[Challenge]:

    statement = (
        select(Challenge)
        .where(Challenge.game_id == game.id)
)

    if status is not None:
        statement = statement.where(
            Challenge.status == status
        )

    if difficulty is not None:
        statement = statement.where(
            Challenge.difficulty == difficulty
        )

    statement = ( # query
        statement
        .order_by(Challenge.id)
        .offset(offset)
        .limit(limit)
    )

    challenges = session.scalars(statement).all()

    return list(challenges)

def get_challenge_by_id(
    session: Session,
    challenge_id: int
) -> Challenge | None:
    return session()