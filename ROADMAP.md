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
- [ ] Add `GET /challenges/{challenge_id}/attempts`
- [ ] Add `PATCH /attempts/{attempt_id}`
- [ ] Add `DELETE /attempts/{attempt_id}`
- [x] Record result, duration, death count, notes, and timestamp
- [ ] Configure and verify cascade deletion

### ORM Features

- [x] Use `session.add()`, `commit()`, `refresh()`, and `delete()`
- [x] Retrieve records with `session.get()`
- [x] Build queries with SQLAlchemy `select()`
- [x] Use `where()`, `offset()`, and `limit()`
- [ ] Load related records without unnecessary queries
- [ ] Add aggregate statistics endpoint
- [ ] Return completion rate and total attempt count

### Migrations

- [ ] Install and initialize Alembic
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