import typing
from datetime import datetime, timedelta

from sqlalchemy import select, update, func, BigInteger, and_, delete

from app.db import session
from app.db.models.movie import MovieModel, MovieSessionModel


async def get_movies_count() -> int:
    query = select(func.count(MovieModel.id))

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalar()


async def get_all_movies(limit: int = 10, offset: int = 0) -> typing.List[MovieModel]:
    query = select(MovieModel).limit(limit).offset(offset)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return list(result.scalars().all())


async def get_movie(movie_id: int) -> MovieModel:
    query = select(MovieModel).where(MovieModel.id == movie_id)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalars().first()


async def create_movie(movie: MovieModel) -> int:
    sess = session.get_async_session()

    sess.add(movie)

    await sess.commit()
    await sess.close()

    return movie.id


async def delete_movie(movie_id: int):
    query = delete(MovieModel).where(MovieModel.id == movie_id)

    sess = session.get_async_session()

    await sess.execute(query)
    await sess.commit()
    await sess.close()


async def get_all_sessions(limit: int, offset: int) -> typing.List[MovieSessionModel]:
    query = select(MovieSessionModel).limit(limit).offset(offset)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return list(result.scalars().all())


async def create_session(movie_session: MovieSessionModel) -> int:
    sess = session.get_async_session()

    sess.add(movie_session)

    await sess.commit()
    await sess.close()

    return movie_session.id


async def delete_session(session_id: int):
    query = delete(MovieSessionModel).where(MovieSessionModel.id == session_id)

    sess = session.get_async_session()

    await sess.execute(query)
    await sess.commit()
    await sess.close()


async def get_active_sessions() -> int:
    query = select(func.count(MovieSessionModel.id)).where(MovieSessionModel.date >= func.current_date())

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalar()


async def get_movies_profit(days: int = 30) -> float:
    profit = 0

    today = datetime.today().date()
    one_month_ago = today - timedelta(days=days)

    query = select(MovieSessionModel).where(MovieSessionModel.date >= one_month_ago)
    sess = session.get_async_session()

    result = await sess.execute(query)
    result = list(result.scalars().all())

    for i in result:
        seats_array = [] if i.seats_busy == "[]" else (
            list(map(int, i.seats_busy.strip("[]").split(", "))))

        profit += i.film.price * len(seats_array)

    await sess.close()

    return profit


async def get_movie_sessions(film_id: int) -> typing.List[MovieSessionModel]:
    query = select(MovieSessionModel).where(MovieSessionModel.film_id == film_id)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return list(result.scalars().all())


async def get_movie_session(session_id: int) -> MovieSessionModel:
    query = select(MovieSessionModel).where(MovieSessionModel.id == session_id)

    sess = session.get_async_session()

    result = await sess.execute(query)

    await sess.close()

    return result.scalars().first()


async def update_movie_session_seats(session_id: int, seats: typing.List[int]):
    seats_str = "[" + ", ".join(map(str, seats)) + "]"

    query = update(MovieSessionModel).where(MovieSessionModel.id == session_id).values(seats_busy=seats_str)

    sess = session.get_async_session()

    await sess.execute(query)
    await sess.commit()
    await sess.close()
