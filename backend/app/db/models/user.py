import uuid
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base

from app.permission import PermissionsEnum, Permissions


class MovieModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    sub: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String(256), nullable=False)

    name: Mapped[str] = mapped_column(String(256), nullable=False)
    given_name: Mapped[str] = mapped_column(String(256), nullable=False)
    family_name: Mapped[str] = mapped_column(String(256), nullable=False)

    picture: Mapped[str] = mapped_column(String(256), nullable=True)

    permission: Mapped[Permissions] = mapped_column(String(256), nullable=True)

    register_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
