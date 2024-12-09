from typing import List, Optional

from fastapi import APIRouter

from app.api.v1.schemas.movie import MovieGetResponse, MovieGetRequest
from app.db.crud import movie

router = APIRouter(prefix="/movies", tags=["main"])


@router.post("/all", response_model=List[MovieGetResponse], response_model_exclude_none=True,
             operation_id="get_movies")
async def get_all_movies(request: Optional[MovieGetRequest] = None):
    request = request if request else MovieGetRequest()

    return await movie.get_all_movies(request.limit, request.offset)
