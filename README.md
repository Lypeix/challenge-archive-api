# Challenge Archive API

Database-backed REST API for gaming challenges, rules, attempts and completions

Assisted by Codex 5.6 Sol

## Technology

- Python
- FastAPI
- SQLAlchemy 2.0
- Pydantic
- SQLite
- Alembic
- pytest
- FastAPI `TestClient`

## Roadmap

### Foundation

- [x] Create GitHub repository and multi-file structure
- [x] Create virtual environment and requirements
- [x] Create FastAPI application
- [x] Configure SQLAlchemy engine
- [ ] Create `DeclarativeBase`
- [ ] Create session factory
- [ ] Add `get_db()` dependency yielding one session per request
- [x] Add application lifespan handler
- [ ] Configure SQLite foreign-key enforcement

### Games

- [ ] Create `Game` SQLAlchemy model
- [ ] Create separate create, update, and response schemas
- [ ] Configure Pydantic `from_attributes=True`
- [ ] Add `POST /games`
- [ ] Add `GET /games`
- [ ] Add `GET /games/{game_id}`
- [ ] Add `PATCH /games/{game_id}`
- [ ] Add `DELETE /games/{game_id}`
- [ ] Add pagination and title/genre filters
- [ ] Return 404 for nonexistent games

### Challenges

- [ ] Create `Challenge` SQLAlchemy model
- [ ] Add foreign key connecting challenges to games
- [ ] Add `Game.challenges` and `Challenge.game` relationships
- [ ] Add challenge status and difficulty validation
- [ ] Add `POST /games/{game_id}/challenges`
- [ ] Add `GET /games/{game_id}/challenges`
- [ ] Add `GET /challenges/{challenge_id}`
- [ ] Add `PATCH /challenges/{challenge_id}`
- [ ] Add `DELETE /challenges/{challenge_id}`
- [ ] Filter challenges by status and difficulty
- [ ] Prevent challenges from referencing nonexistent games

### Attempts

- [ ] Create `Attempt` SQLAlchemy model
- [ ] Connect attempts to challenges through a foreign key
- [ ] Configure challenge-attempt relationships
- [ ] Add `POST /challenges/{challenge_id}/attempts`
- [ ] Add `GET /challenges/{challenge_id}/attempts`
- [ ] Add `PATCH /attempts/{attempt_id}`
- [ ] Add `DELETE /attempts/{attempt_id}`
- [ ] Record result, duration, death count, notes, and timestamp
- [ ] Configure and verify cascade deletion

### ORM Features

- [ ] Use `session.add()`, `commit()`, `refresh()`, and `delete()`
- [ ] Retrieve records with `session.get()`
- [ ] Build queries with SQLAlchemy `select()`
- [ ] Use `where()`, `offset()`, and `limit()`
- [ ] Load related records without unnecessary queries
- [ ] Add aggregate statistics endpoint
- [ ] Return completion rate and total attempt count

### Migrations

- [x] Install and initialize Alembic
- [ ] Connect Alembic to SQLAlchemy metadata
- [ ] Generate initial migration
- [ ] Apply migration to a clean database
- [ ] Replace development `create_all()` with migrations
- [ ] Document migration commands

### Testing

- [ ] Create isolated SQLAlchemy test engine
- [ ] Override FastAPI `get_db()` dependency during tests
- [ ] Test successful game CRUD
- [ ] Test challenge and attempt relationships
- [ ] Test cascade deletion
- [ ] Test filters and pagination
- [ ] Test 404 responses
- [ ] Test Pydantic 422 responses
- [ ] Test statistics calculations

### Documentation

- [ ] Add installation and startup instructions
- [ ] Add database migration instructions
- [ ] Add endpoint examples
- [ ] Add project structure
- [ ] Add architecture explanation
- [ ] Document known limitations
- [ ] Complete development log

## Structure


```text
challenge-archive-api/
|-- alembic/
|   |-- versions/
|   |-- env.py
|   |-- README
|   `-- script.py.mako
|-- app/
|   |-- routers/
|   |   |-- __init__.py
|   |   |-- attempts.py
|   |   |-- challenges.py
|   |   |-- games.py
|   |   `-- stats.py
|   |-- __init__.py
|   |-- crud.py
|   |-- database.py
|   |-- main.py
|   |-- models.py
|   `-- schemas.py
|-- tests/
|   |-- conftest.py
|   |-- test_attempts.py
|   |-- test_challenges.py
|   |-- test_games.py
|   `-- test_stats.py
|-- .gitignore
|-- alembic.ini
|-- DEVLOG.md
|-- README.md
`-- requirements.txt
        