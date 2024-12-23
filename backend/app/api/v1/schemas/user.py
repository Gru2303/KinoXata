from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime

from app.api.v1.schemas.movie import MovieResponse


class UserMeResponse(BaseModel):
    id: int
    email: str
    name: str
    picture: str
    permission: str
    register_time: datetime


class UserTicketSignRequest(BaseModel):
    sign: str


class UserTicketResponse(BaseModel):
    id: int
    film: MovieResponse
    seats: List[int]
    date: datetime
    secret: str
