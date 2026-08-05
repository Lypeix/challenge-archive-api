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
- Added pathing to database.py
- Created database URL
- Configured SQLAlchemy engine in database.py
- Added few comments
- Implemented foreign keys
- Established DeclarativeBase
- Made session factory
- Added get_db() yielding one session per request
- Finished app lifespan handler in main.py
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
- Imported required tech to models.py
- Built class Game(Base) in models.py
- Added explanatory comments
- Added guaranteed db cleanup w try/finally to app lifespan handler in main.py
- Added GameBase, GameCreate, GameUpdate, GameResponse schemas to schemas.py
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
- Fixed some typos

### SESSION 2 (22:12-22:54)
- Created the `POST /games` endpoint in `games.py`
- Registered the games router in `main.py`
- Successfully tested `POST /games` through Swagger UI
- Added explanatory comments for every new LOC in `games.py`

## DAY 9 - 04.08.2026
- Added German Devlog titled `LERNPROTOKOLL_DE.md` reskinned-reconstruction
- Split `README.md` into `README.md` n `ROADMAP.md`

## DAY 10 - 05.08.2026
### SESSION 1 (18:57-x)
- Created reconstruction file
- Reconstructed imports from memory
- Reconstructed `Game` Pydantic model from memory
- Added explanatory comments