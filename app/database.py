from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_PATH = (
    Path(__file__).resolve().parent.parent # double parent cause db.py belongs to app folder which belongs to challenge-archive-api folder
    / "challenge-archive.db"
)

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}" # converts filesystem location into SQLAlchemy connection URL

engine = create_engine( # knows which db system is being used, where db is, manages connections, gives sessions access to the db
    DATABASE_URL,
    connect_args={"check_same_thread": False} # allows connection to be used across different threads
                                              # thread is an executor that handles requests sent to endpoints
)
