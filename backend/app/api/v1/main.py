from fastapi import APIRouter

from .routers import movie
from .routers import login

router = APIRouter(prefix="/api/v1", tags=["main"])


router.include_router(
	login.router,
	tags=["login"]
)

router.include_router(
	movie.router,
	tags=["movie"]
)