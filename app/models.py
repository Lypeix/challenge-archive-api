from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Game(Base):
    __tablename__ = "games" # tells SQLAlchemy which db table this model represents

    id: Mapped[int] = mapped_column( # id is ORM-mapped attribute whose Python value is an int
                                     # Mapped[int] describes the python-side type n tells ORM this attribute belongs to mapping
                                     # mapped_column() defines db column settings
        
        primary_key=True # means every row has unique id
    )

    title: Mapped[str] = mapped_column(
        String(100), # defines db column as string text with max character length of 100
        nullable=False, # means db cannot store NULL in the title column (though pydantic is still helpful for validating stuff like whitespace-only string"
        index=True # tells SQLAlchemy to create idx for the title column
    )

    genre: Mapped[str] = mapped_column(
        String(50),
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

    challenges: Mapped[list["Challenge"]] = relationship( # creates challenges attributes for games (games.challenges), it contains Challenge objects for particular game
        back_populates="game",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    game_id: Mapped[int] = mapped_column(
        ForeignKey(
            "games.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    rules: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="planned",
        server_default="planned",
        index=True
    )

    difficulty: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    game: Mapped["Game"] = relationship(
        back_populates="challenges"
    )

    attempts: Mapped[list["Attempt"]] = relationship(
        back_populates="challenge",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(
        primary_key=True 
    )

    challenge_id: Mapped[int] = mapped_column(
        ForeignKey(
            "challenges.id",
            ondelete="CASCADE"
            ),
            nullable=False,
            index=True
        )


    result: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )


    duration_minutes: Mapped[int] = mapped_column(
        nullable=False
    )


    death_count: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default="0"
    )


    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    challenge: Mapped["Challenge"] = relationship(
        back_populates="attempts"
    )