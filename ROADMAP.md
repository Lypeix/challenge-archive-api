## Roadmap

### Foundation

- [x] Create GitHub repository and multi-file structure
- [x] Create virtual environment and requirements
- [x] Create FastAPI application
- [x] Configure SQLAlchemy engine
- [x] Create `DeclarativeBase`
- [x] Create session factory
- [x] Add `get_db()` dependency yielding one session per request
- [x] Add application lifespan handler
- [x] Configure SQLite foreign-key enforcement

### Games

- [x] Create `Game` SQLAlchemy model
- [x] Create separate create, update, and response schemas
- [x] Configure Pydantic `from_attributes=True`
- [x] Add `POST /games`
- [x] Add `GET /games`
- [x] Add `GET /games/{game_id}`
- [x] Add `PATCH /games/{game_id}`
- [x] Add `DELETE /games/{game_id}`
- [x] Add pagination and title/genre filters
- [x] Return 404 for nonexistent games

### Challenges

- [x] Create `Challenge` SQLAlchemy model
- [x] Add foreign key connecting challenges to games
- [x] Add `Game.challenges` and `Challenge.game` relationships
- [x] Add challenge status and difficulty validation
- [x] Add `POST /games/{game_id}/challenges`
- [x] Add `GET /games/{game_id}/challenges`
- [x] Add `GET /challenges/{challenge_id}`
- [x] Add `PATCH /challenges/{challenge_id}`
- [x] Add `DELETE /challenges/{challenge_id}`
- [x] Filter challenges by status and difficulty
- [x] Prevent challenges from referencing nonexistent games

### Attempts

- [x] Create `Attempt` SQLAlchemy model
- [x] Connect attempts to challenges through a foreign key
- [x] Configure challenge-attempt relationships
- [x] Create Pydantic schemas for Attempts
- [x] Add `POST /challenges/{challenge_id}/attempts`
- [x] Add `GET /challenges/{challenge_id}/attempts`
- [x] Add `PATCH /attempts/{attempt_id}`
- [x] Add `DELETE /attempts/{attempt_id}`
- [x] Record result, duration, death count, notes, and timestamp
- [x] Configure and verify cascade deletion

### Migrations

- [x] Install and initialize Alembic
- [x] Connect Alembic to SQLAlchemy metadata
- [x] Generate and apply initial migration to a clean database
- [x] Remove development `create_all()`
- [x] Document migration commands

### Testing

- [x] Create isolated test database and override `get_db()`
- [x] Test successful game CRUD
- [x] Test challenge and attempt relationships
- [x] Test cascade deletion
- [ ] Test filters and pagination
- [ ] Test representative `404` and `422` responses

### Documentation

- [ ] Complete README with project overview, local setup, migrations, and structure
- [ ] Complete development log