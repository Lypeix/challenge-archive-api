# Challenge Archive API


A database-backed REST API for recording video games, defining gaming challenges, and tracking individual attempts.

The project demonstrates relational data modelling, validated API design, database migrations, nested resources, cascade deletion, filtering, pagination, and isolated integration testing.

## Resource Model

```text
Game
`-- Challenge
    `-- Attempt

## Technology

- Python
- FastAPI
- SQLAlchemy 2.0
- Pydantic
- SQLite
- Alembic
- pytest
- FastAPI `TestClient`

## Database Migrations

Database schema is managed with Alembic

To apply available migrations:

```powershell
py -m alembic upgrade head
```

To create a new migration after changing SQLAlchemy models:

```powershell
py -m alembic revision --autogenerate -m "description"
```

To check current migration:

```powershell
py -m alembic current
```

To check whether the database schema is up-to-date with SQLAlchemy models:

```powershell
py -m alembic check
```

To revert the latest migration:

```powershell
py -m alembic downgrade -1
```

challenge-archive-api/
|-- alembic/
|   |-- env.py
|   |-- README
|   |-- script.py.mako
|   `-- versions/
|
|-- app/
|   |-- routers/
|   |   |-- __init__.py
|   |   |-- attempts.py
|   |   |-- challenges.py
|   |   `-- games.py
|   |
|   |-- __init__.py
|   |-- crud.py
|   |-- database.py
|   |-- main.py
|   |-- models.py
|   `-- schemas.py
|
|-- tests/
|   |-- conftest.py
|   |-- test_challenges.py
|   `-- test_games.py
|
|-- .gitignore
|-- alembic.ini
|-- DEVLOG.md
|-- README.md
|-- requirements.txt
`-- ROADMAP.md
         