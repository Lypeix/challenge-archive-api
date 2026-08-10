# !DEVLOG!

## DAY 1 - 27.07.2026
### SESSION 1 (15:12-16:35)
- Created GitHub repo
- Created multi-file structure
- Created .gitignore
- Created virtual environment for localized installations
- Created requirements
- Installed required tech

## DAY 2 - 28.07.2026
### SESSION 1 (19:55-21:01)
- Created FastAPI app instance
- Added app lifespan handler foundation
- Added pathing to `database.py`
- Created `database URL`
- Configured SQLAlchemy engine in `database.py`
- Added few comments
- Implemented foreign keys
- Established DeclarativeBase
- Made session factory
- Added `get_db()` yielding one session per request
- Finished app lifespan handler in `main.py`
- Added more space between comments
- Fixed typos

## DAY 3 - 29.07.2026
### BREAK DAY

## DAY 4 - 30.07.2026
### Note: From 1st to 3rd of August, I will be on a vacation trip to Krynica.
### SESSION 1 (21:20-22:42)
### Every reconstruction was completed in `reskinned-reconstruction/database.py` n includes explanatory comment
- Reconstructed imports 
- Reconstructed DATABASE_PATH 
- Reconstructed DATABASE_URL
- Reconstructed engine
- Reconstructed foreign-key enforcement
- Fixed foreign-key enforcement explanatory comment in the actual db file
- Reconstructed DeclarativeBase class
- Reconstructed session factory
- Reconstructed the db session dependency

## DAY 5 - 31.07.2026
### SESSION 1 (15:53-16:57)
- Imported required tech to `models.py`
- Built class Game(Base) in `models.py`
- Added explanatory comments
- Added guaranteed db cleanup w try/finally to app lifespan handler in `main.py`
- Added `GameBase`, `GameCreate`, `GameUpdate`, `GameResponse` schemas to `schemas.py`
- Successfully tested the schemas in PowerShell
- Created foundation for the Post endpoint

## DAY 6-7 - 01-02.08.2026
- Project paused because of vacation trip to Krynica

## DAY 8 - 03.08.2026
### SESSION 1 (20:41-21:43)
- Renamed files in `reskinned-reconstruction` (they were identical to the ones from actual code)
- Reconstructed whole `models.py` as `models_reskin.py`
- Explained the entire reconstruction with comments next to particular LOCs (lines of code, not sunglasses)
- Refined n corrected earlier comments
- Fixed typos

### SESSION 2 (22:12-22:54)
- Created the `POST /games` endpoint in `games.py`
- Registered the games router in `main.py`
- Successfully tested `POST /games` through Swagger UI
- Added explanatory comments for every new LOC in `games.py`

## DAY 9 - 04.08.2026
- Added German Devlog titled `LERNPROTOKOLL_DE.md` reskinned-reconstruction
- Split `README.md` into `README.md` n `ROADMAP.md`

## DAY 10 - 05.08.2026
### SESSION 1 (18:57-19:40)
- Created reconstruction file
- Reconstructed imports from memory
- Reconstructed `GameBase` Pydantic model from memory
- Added explanatory comments
- Reconstructed missing `GameBase` model field n validation pieces from memory
- Reconstructed `GameCreate` model from memory
- Reconstructed `GameUpdate` model from memory
- Reconstructed `GameResponse` model from memory

### SESSION 2 (21:06-22:00)
- Reconstructed imports in `crud.py` from memory
- Reconstructed `create_game` from memory
- Added explanatory comments
- Checked out different parameters:
    - name: Type       # Expected type
    - name = value     # Default value
    - name: Type = x   # Expected type plus default value
- Reconstructed imports in `routers/games.py` from memory
- Reconstructed games router from memory 
- Reconstructed games POST endpoint from memory
- Reconstructed `create_game` inside `routers/games.py`

## DAY 11 - 06.08.2026
- Updating and expanding the documentation of space-obeservatory-api

## DAY 12 - 07.08.2026
### SESSION 1 (16:50-18:00)
- Fixed alembic folder structure
- Updated structure tree in README
- String limits for title n genre in `models.py` now share the same value with `schemas.py` string limits
- Fixed comment for what a session is in line 34 of `database.py`
- Revised earlier material:
    - for example ORM exists to map Python objects to database tables/rows n translate changes to mapped objects into the correct database operations
- Implemented `get_games` n `get_game_by_id` to `crud.py`
- Created `list_games` n `get_game_by_id` router endpoints to `app/routers/games.py`
- Raised HTTPException status code ERROR 404 for `get_game_by_id` incase there's no game with matching id
- Successfully tested the new endpoints

## DAY 13 - 08.08.2026
### SESSION 1 (10:44-12:00)
- Implemented `update_game()` to `crud.py`
- Wired `update_game()` to the PATCH endpoint in `app/routers/games.py`
- Successfuly tested whole sequence through SwaggerUI
- Implemented `delete_game()` to `crud.py`
- Wired `delete_game()` to DELETE endpoint in `app/routers/games.py`
- Tested the new endpoint through SwaggerUI
- Polished earlier documentation
- Created offset-based pagination in `get_games()`
- Added validated `offset` and `limit` pagination to the `GET /games` endpoint in `app/routers/games.py`
- Added title/genre filters to the `GET /games` endpoint in `app/routers/games.py`
- Successfully tested pagination and filters through SwaggerUI

## DAY 14 - 09.08.2026
### SESSION 1 (15:18-15:41)
- Created `Challenge(Base)` model in `models.py`
- Created `Game.challanges` and `Challenge.game` relationships in `models.py`

### SESSION 2 (22:42-22:54)
- Debugged `statement` in `crud.py`
- Added`response_model=GameResponse` to the single-game endpoint in `games.py` 
- Updated optional list-games query parameters in `games.py` to say str | None instead of str

## DAY 15 - 10.08.2026
### SESSION 1 (09:19-10:05)
- Added challenge status and difficulty validation in `schemas.py`
- Created `ChallengeStatus`, `ChallengeDifficulty` string enums
- Created `ChallengeBase`, `ChallengeCreate`, `ChallengeUpdate`, `ChallengeResponse` inside `schemas.py`
- Implemented `create_challenge()` in `crud.py`
- Wired challenge creation to `POST /games/{game_id}/challenges`
- Prevented challenges from referencing non-existent games
- Successfully tested the creations, 422 and 404 responses, and Pydantic validation through SwaggerUI

### SESSION 2 (12:36-13:35)
- Constructed `list_challenges` in `crud.py`
- Added `GET /games/{game_id}/challenges`
- Added filtering by challenge status and difficulty
- Verified parent-game isolation
- Successfuly tested listing, filtering and status codes through SwaggerUI
- Reviewed relational SQLAlchemy queries