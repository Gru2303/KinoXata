from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime


class AdminUserRequest(BaseModel):
    limit: Optional[int] = 10
    offset: Optional[int] = 0


class AdminUserSetRequest(BaseModel):
    id: int
    admin: bool


class AdminStatsResponse(BaseModel):
    users: int
    films: int
    sessions: int
    tickets_sell: int
    month_money: float
    week_money: float
