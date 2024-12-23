from typing import List, Optional

from fastapi import APIRouter

from app.api.v1.schemas.movie import MovieResponse, MoviesRequest, MovieRequest, MovieSessionsRequest, \
    MovieSessionsResponse
from app.db.crud import movie

router = APIRouter(prefix="/movies", tags=["main"])


@router.post("/all", response_model=List[MovieResponse], response_model_exclude_none=True,
             operation_id="get_movies")
async def get_all_movies(request: Optional[MoviesRequest] = None):
    request = request if request else MoviesRequest()

    return await movie.get_all_movies(request.limit, request.offset)


@router.post("/movie", response_model=MovieResponse, response_model_exclude_none=True,
             operation_id="get_movie")
async def get_all_movies(request: MovieRequest):
    return await movie.get_movie(request.id)


@router.post("/movie/sessions", response_model=List[MovieSessionsResponse], response_model_exclude_none=True,
             operation_id="get_movie_sessions")
async def get_all_movies(request: MovieSessionsRequest):
    return await movie.get_movie_sessions(request.id)
