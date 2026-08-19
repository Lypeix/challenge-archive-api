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

# registers functions below as pytest fixture
# fixture prepares smth required for tests
@pytest.fixture 
def client(tmp_path):
# defines fixture
# tmp_path is a built-in pytest fixture 
# pytest sees the parameter name n supplies temp Path directory
    
    test_database_path = tmp_path / "test_db"

    test_engine = create_engine(
    # creates sqlalchemy engine that will work within the temp database

        f"sqlite:///{test_database_path.as_posix()}",
        connect_args={"check_same_thread": False}
    )
