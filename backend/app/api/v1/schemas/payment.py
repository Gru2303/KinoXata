from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime


class PaymentProcessRequest(BaseModel):
    session_id: int

    seats: List[int]

    card_number: str
    card_name: str
    card_exp: str
    card_cvv: str


class PaymentProcessResponse(BaseModel):
    success: bool
    message: Optional[str] = None
