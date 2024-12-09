from sqlalchemy import Engine, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings
from app.db.models.base import Base


def new_async_engine() -> AsyncEngine:
    return create_async_engine(
        URL.create(
            drivername="postgresql+asyncpg",
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
            username=settings.DATABASE_USERNAME,
            password=settings.DATABASE_PASSWORD.get_secret_value(),
            database=settings.DATABASE_DB,
        ),
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        pool_timeout=30.0,
        pool_recycle=600
    )


_ASYNC_ENGINE = new_async_engine()
_ASYNC_SESSIONMAKER = async_sessionmaker(_ASYNC_ENGINE, expire_on_commit=False)


def get_async_engine() -> AsyncEngine:
    return _ASYNC_ENGINE


def get_async_session() -> AsyncSession:
    return _ASYNC_SESSIONMAKER()


async def create_tables():
    async with get_async_engine().begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
