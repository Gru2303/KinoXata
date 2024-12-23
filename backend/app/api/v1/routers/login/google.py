from typing import Optional

from fastapi import APIRouter

import requests
from requests import session
from starlette.responses import Response, RedirectResponse

from app.config import settings
from app.api.v1.schemas.login.google import GoogleLoginResponse, GoogleHTTPErrorCode

from app.db.crud import user
from app.db.crud.token import create_token

router = APIRouter()


@router.get("/",
            response_model=GoogleLoginResponse,
            response_model_exclude_none=True,
            operation_id="get_google_login_url")
async def get_google_login_url():
    scope = "openid email profile"

    return GoogleLoginResponse(url=
                               f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.GOOGLE_CLIENT_ID}&"
                               f"response_type=code&scope={scope}&"
                               "redirect_uri=http://localhost:8000/api/v1/login/google/callback")


@router.get("/callback",
            # response_model=GoogleLoginResponse,
            response_model_exclude_none=True,
            operation_id="google_login_callback",
            responses=GoogleHTTPErrorCode.responses())
async def get_google_login_url(code: Optional[str] = None):
    if not code:
        return GoogleHTTPErrorCode.INVALID_CODE.response()

    token_endpoint = "https://oauth2.googleapis.com/token"
    payload = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": "http://localhost:8000/api/v1/login/google/callback",
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_endpoint, data=payload)

    if token_response.status_code != 200:
        return GoogleHTTPErrorCode.INVALID_GOOGLE_RESPONSE.response()

    token_data = token_response.json()
    id_token = token_data.get("id_token")

    if not id_token:
        return GoogleHTTPErrorCode.INVALID_GOOGLE_ID_TOKEN.response()

    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {token_data.get('access_token')}"}
    )

    if user_info_response.status_code != 200:
        return GoogleHTTPErrorCode.INVALID_GOOGLE_USER_INFO_RESPONSE.response()

    user_info = user_info_response.json()

    user_data = await user.get_user(user_info.get("sub"))

    if not user_data:
        user_data = await user.create_user(user.UserModel(
            platform_id=user_info.get("sub"),
            email=user_info.get("email"),
            name=user_info.get("name"),
            picture=user_info.get("picture")
        ))

    raw_token, token = await create_token(user_data)

    response = RedirectResponse("http://localhost/", status_code=301)

    response.set_cookie("auth_token", raw_token, httponly=True, secure=True, samesite="strict")

    return response
