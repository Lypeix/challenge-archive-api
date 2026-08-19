import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from app.database import (
    Base,
    enable_sqlite_foreign_keys, 
    get_db
    )
from app.main import app

# registers the function below as pytest fixture
# fixture prepares smth required for tests
@pytest.fixture 
def client(tmp_path):
    # defines fixture
    # tmp_path supplies a unique temporary Path directory for each test
    
    test_database_path = tmp_path / "test_db"

    test_engine = create_engine(
    # creates sqlalchemy engine that will work within the temp database

        f"sqlite:///{test_database_path.as_posix()}",
        connect_args={"check_same_thread": False}
    )

    event.listen(
        test_engine, # target, listens for event that occur on the test engine
        "connect", # event_name, runs something whenever engine opens database connection
        enable_sqlite_foreign_keys # function, runs existing function from database.py when connection is opened
    )

    TestingSessionLocal = sessionmaker( # creates a session factory
        bind=test_engine, # uses this engine to create sessions 
        expire_on_commit=False # matches SessionLocal from actual database
    )

    Base.metadata.create_all(bind=test_engine) # every model in models.py inherits from Base so SQLAlchemy collects their table definitions inside Base.metadata

    def override_get_db():
        with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db # no parantheses so that fastapi calls them when they should be called instead of calling them immedietaly

    try:
        with TestClient(app) as test_client: # creates a client that can send simulated HTTP requests to the app
            yield test_client # gives TestClient to whichever test requested the fixture
    finally:
        app.dependency_overrides.clear() # removes test dependency override after the test finishes
        test_engine.dispose() # closes test engine database connection, allowing temp files to be cleared up