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


@event.listens_for(engine, "connect") # this decorator runs the function below whenever engine establishes a new SQLite connection
def enable_sqlite_foreign_keys(
    dbapi_connection, # sqlite3 connection
    
    _connection_record # stores SQLAlchemy's info abt dbapi_connection
):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA FOREIGN_KEYS = ON") # Makes SQLite reject references to non-existent rows 
    cursor.close()

class Base(DeclarativeBase): # base becomes the parent class for every SQLAlchemy model
    pass 

SessionLocal = sessionmaker( # creates sessions, which execute queries, tracks ORM objects n manages transactions 
    
    bind=engine, # every session made by Sessionlocal uses the previously configured engine

    expire_on_commit=False # True is default because SQLAlchemy marks values as possibly outdated, so it reloads them when used again 
                          # keeps the values available after already saving/commiting. No idea why use false yet, I'll find out next session
)

def get_db(): 
    with SessionLocal() as session:
        yield session # gives session to endpoint > func pauses > endpoint handles client request > endpoint finishes > func resumes