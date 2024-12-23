from fastapi import APIRouter

from .routers import movie
from .routers import login
from .routers import user
from .routers import payment
from .routers.admin import admin

router = APIRouter(prefix="/api/v1", tags=["main"])


router.include_router(
	login.router,
	tags=["login"]
)

router.include_router(
	movie.router,
	tags=["movie"]
)

router.include_router(
	user.router,
	tags=["user"]
)

router.include_router(
	payment.router,
	tags=["payment"]
)

router.include_router(
	admin.router,
	tags=["admin"]
)
