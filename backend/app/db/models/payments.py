from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base
from .movie import MovieModel


class PaymentModel(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)

    ticket_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("tickets.id"), nullable=False)

    card_number: Mapped[str] = mapped_column(String(256), nullable=False)
    card_name: Mapped[str] = mapped_column(String(256), nullable=False)

    cost: Mapped[int] = mapped_column(BigInteger, nullable=False)

    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("UserModel", lazy="selectin")

    ticket = relationship("UserTicketModel", lazy="selectin")
