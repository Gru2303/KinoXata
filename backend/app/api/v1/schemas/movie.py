from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime


class MovieRequest(BaseModel):
	id: int


class MovieSessionRequest(BaseModel):
	id: int


class MoviesRequest(BaseModel):
	limit: Optional[int] = 10
	offset: Optional[int] = 0


class MoviesSessionsAdminRequest(BaseModel):
	limit: Optional[int] = 10
	offset: Optional[int] = 0


class MovieSessionsRequest(BaseModel):
	id: int


class MovieAddRequest(BaseModel):
	title: str
	description: str

	image: str
	afisha_image: str

	lang: str

	genre: str

	time: str

	trailer: str

	price: int


class MovieResponse(BaseModel):
	id: int

	title: str
	description: str

	image: str
	afisha_image: str

	lang: str

	genre: str

	time: str

	trailer: str

	price: int

	create_time: datetime
	update_time: datetime


class MovieSessionsAddRequest(BaseModel):
	film_id: int

	seats: int

	date: datetime


class MovieSessionsResponse(BaseModel):
	id: int

	film_id: int

	seats: int
	seats_busy: str

	date: datetime

	create_time: datetime
	update_time: datetime
