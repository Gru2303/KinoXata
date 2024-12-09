from enum import Enum

from pydantic import BaseModel

from app.api.v1.schemas.error import ErrorResponse, ErrorResponseEnum


class GoogleHTTPErrorCode(ErrorResponseEnum):
    INVALID_CODE = (400, "Invalid code")
    INVALID_GOOGLE_RESPONSE = (400, "Invalid response from Google")
    INVALID_GOOGLE_ID_TOKEN = (400, "Invalid Google id token")
    INVALID_GOOGLE_USER_INFO_RESPONSE = (400, "Invalid user info response from Google")


class GoogleLoginResponse(BaseModel):
    login_url: str
