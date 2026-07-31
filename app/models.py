from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Game(Base):
    __tablename__ = "games" # tells SQL which db table this model represents

    id: Mapped[int] = mapped_column( # id is ORM-mapped attribute whose Python value is an int
                                     # Mapped[int] describes the python-side type n tells ORM this attribute belongs to mapping
                                     # mapped_column() defines db column settings
        
        primary_key=True # means every row has unique id
    )

    title: Mapped[str] = mapped_column(
        String(150), # defines db column as string text with max character length of 150
        nullable=False, # means db cannot store NULL in the title column (though pydantic validation for whitespaces n other bypasses is still needed)
        index=True # tells SQL to create idx for the title column
    )

    genre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True
    )

    release_year: Mapped[int] = mapped_column(
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )