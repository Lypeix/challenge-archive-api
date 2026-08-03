from datetime import datetime # imports Python's date n time class

from sqlalchemy import DateTime, String, func # DateTime tells SQLAlchemy that the db column stores date n time values
                                              # String - db-side string
                                              # func gives access to the SQL functions

from sqlalchemy.orm import Mapped, mapped_column # Mapped marks attribute as belonging to the ORM Mapping (python-side)
                                                 # mapped_column defines the db column config for a mapped attribute 

from app.database import Base # Base subclasses r registered as ORM models

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(


        primary_key=True # without this, ORM may refuse to map a model
    )

    title: Mapped[str] = mapped_column(
        String(150), # char limit
        nullable=False, # title must not be SQL NULL (SQL must recognize the value)
        index=True # index for filtering titles, eg. title = "Dark Souls" alongside the primary_key numeric lookup
)
    genre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True 
    )

    release_year: Mapped[int] = mapped_column( # non-Null int column
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), # makes a datetime column intended to preserve timezone info
        server_default=func.now(), # db auto-generates current time if INSERT omits created_at
        nullable=False
    )
