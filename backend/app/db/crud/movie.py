import typing

from sqlalchemy import select

from app.db import session
from app.db.models.movie import MovieModel


async def get_all_movies(limit: int = 10, offset: int = 0) -> typing.List[MovieModel]:
	query = select(MovieModel).limit(limit).offset(offset)

	sess = session.get_async_session()

	result = await sess.execute(query)

	return list(result.scalars().all())

