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
|-- requirements.txt
`-- ROADMAP.md
        