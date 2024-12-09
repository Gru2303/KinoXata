from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime


class MovieGetRequest(BaseModel):
	limit: Optional[int] = 10
	offset: Optional[int] = 0


class MovieGetResponse(BaseModel):
	id: int
	name: str
	title: str
	image: Optional[str] = None
	afisha_image: Optional[str] = None

	create_time: datetime
	update_time: datetime
