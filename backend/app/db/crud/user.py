import typing
import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

from sqlalchemy import select, insert, func, update

from app.config import settings
from app.db import session
from app.db.models.user import UserModel, UserTicketModel
from app.permission import Permissions
from app.user.permission import UserPermissions


async def create_user(user: UserModel) -> UserModel:
    sess = session.get_async_session()

    sess.add(user)

    await sess.commit()

    return user


async def get_users_count() -> int:
    query = select(func.count(UserModel.id))

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalar()


async def get_all_users(limit: int = 10, offset: int = 0) -> typing.List[UserModel]:
    query = select(UserModel).limit(limit).offset(offset)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return list(result.scalars().all())


async def get_user(platform_id: str) -> UserModel:
    query = select(UserModel).where(UserModel.platform_id == platform_id)

    sess = session.get_async_session()

    result = await sess.execute(query)

    return result.scalars().first()


async def set_user_admin(user_id: int, admin: bool = False):
    permission = Permissions[UserPermissions]("ffffffffffffffff") if admin \
        else Permissions[UserPermissions](Permissions.DEFAULT_PERMISSIONS)
    query = update(UserModel).where(UserModel.id == user_id).values(permission=permission)

    sess = session.get_async_session()

    await sess.execute(query)
    await sess.commit()
    await sess.close()


async def get_tickets_count() -> int:
    query = select(func.count(UserTicketModel.id))

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalar()


async def create_ticket(user_id: int, session_id: int, seats: typing.List[int]) -> int:
    seats_str = "[" + ", ".join(map(str, seats)) + "]"

    private_key = load_pem_private_key(settings.PRIVATE_KEY.encode("utf-8"), None)

    raw = f"{user_id}--{session_id}--{seats_str}"

    print(raw)

    public_key_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Виводимо у PEM-форматі
    print(public_key_pem.decode('utf-8'))

    secret = raw + "###" + base64.b64encode(private_key.sign(raw.encode("utf-8"))).decode("utf-8")

    print(secret)

    model = UserTicketModel(
        user_id=user_id, session_id=session_id,
        seats_busy=seats_str, secret=secret
    )

    sess = session.get_async_session()

    sess.add(model)

    await sess.commit()
    await sess.close()

    return model.id


async def get_all_tickets(user_id: int) -> typing.List[UserTicketModel]:
    query = select(UserTicketModel).where(UserTicketModel.user_id == user_id).order_by(UserTicketModel.id.desc())

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return list(result.scalars().all())


async def get_ticket_by_sign(sign: str) -> UserTicketModel:
    query = select(UserTicketModel).where(UserTicketModel.secret == sign)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalars().first()