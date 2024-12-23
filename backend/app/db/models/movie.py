from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base


class MovieModel(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(String(512), nullable=True)

    image: Mapped[str] = mapped_column(String(256), nullable=True)
    afisha_image: Mapped[str] = mapped_column(String(256), nullable=True)

    trailer: Mapped[str] = mapped_column(String(256), nullable=True)

    lang: Mapped[str] = mapped_column(String(256), nullable=True)

    genre: Mapped[str] = mapped_column(String(256), nullable=True)

    time: Mapped[str] = mapped_column(String(20), nullable=True)

    price: Mapped[int] = mapped_column(BigInteger, nullable=False)


class MovieSessionModel(Base):
    __tablename__ = "movie_sessions"

    id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True)

    film_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("movies.id"), nullable=False)

    seats: Mapped[int] = mapped_column(BigInteger, nullable=False)

    seats_busy: Mapped[str] = mapped_column(String(256), nullable=True)

    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    film: Mapped[MovieModel] = relationship(lazy="selectin")
