from fastapi import APIRouter
from starlette.responses import RedirectResponse

from . import google

router = APIRouter(prefix="/login", tags=["main"])

router.include_router(
    google.router,
    prefix="/google",
    tags=["google", "login"]
)


@router.post("/unauthorized")
async def unauthorized():
    return {"detail": "Unauthorized"}