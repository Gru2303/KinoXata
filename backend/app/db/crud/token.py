import hashlib
import secrets
import string

from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

from sqlalchemy import select, update
from sqlalchemy.orm import Mapped

from app.db import session
from app.db.models.token import TokenModel
from app.db.models.user import UserModel


async def create_token(user: UserModel, lifespan: int = 7) -> (str, TokenModel):
    raw_token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(128))
    hashed_token = hashlib.sha256(raw_token.encode()).hexdigest()

    expires_at = datetime.now() + timedelta(days=lifespan)

    new_token = TokenModel(
        user_id=user.id,
        token_hash=hashed_token,
        expires_at=expires_at,
    )

    sess = session.get_async_session()

    sess.add(new_token)

    await sess.commit()

    return raw_token, new_token


async def verify_token(token: str) -> UserModel or None:
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    query = select(TokenModel).where(TokenModel.token_hash == hashed_token, TokenModel.is_active == True)

    sess = session.get_async_session()

    result = await sess.execute(query)
    result = result.scalars().first()

    await sess.close()

    if result and result.is_active and result.expires_at > datetime.now(timezone.utc):
        return result.user

    return None


async def get_token(token: str) -> TokenModel:
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    query = select(TokenModel).where(TokenModel.token_hash == hashed_token)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalars().first()


async def deactivate_token(token: str) -> None:
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    query = update(TokenModel).where(TokenModel.token_hash == hashed_token).values(is_active=False)

    sess = session.get_async_session()

    await sess.execute(query)
    await sess.commit()
    await sess.close()
