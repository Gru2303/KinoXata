from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base

from app.db.types.permission import PermissionsType

from app.permission import PermissionsEnum, Permissions
from app.user.permission import UserPermissions
from .movie import MovieSessionModel
from .payments import PaymentModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True, index=True)

    platform_id: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    email: Mapped[str] = mapped_column(String(256), nullable=False)

    name: Mapped[str] = mapped_column(String(256), nullable=False)

    picture: Mapped[str] = mapped_column(String(256), nullable=True)

    permission: Mapped[Permissions[UserPermissions]] = mapped_column(PermissionsType,
                                                                     server_default=Permissions.DEFAULT_PERMISSIONS)

    register_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class UserTicketModel(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)

    session_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("movie_sessions.id"), nullable=False)

    seats_busy: Mapped[str] = mapped_column(String(256), nullable=True)

    secret: Mapped[str] = mapped_column(String(512), nullable=False)

    user: Mapped[UserModel] = relationship(lazy="selectin")

    session: Mapped[MovieSessionModel] = relationship(lazy="selectin")

