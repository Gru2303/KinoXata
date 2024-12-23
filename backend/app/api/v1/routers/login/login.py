from typing import Any, Coroutine

from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from app.db.crud.token import verify_token, deactivate_token
from app.db.models.user import UserModel
from . import google

router = APIRouter(prefix="/login", tags=["main"])

router.include_router(
    google.router,
    prefix="/google",
    tags=["google", "login"]
)


@router.post("/unauthorized", operation_id="unauthorized")
async def unauthorized(request: Request):
    token = request.cookies.get("auth_token")

    if token:
        await deactivate_token(token)

    response = Response()

    response.delete_cookie("auth_token")

    return response


async def get_auth_user(request: Request) -> UserModel:
    token = request.cookies.get("auth_token")

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = await verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user
