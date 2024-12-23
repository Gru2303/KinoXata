from typing import List, Optional

from fastapi import APIRouter, Depends

from app.api.v1.routers.login import get_auth_user
from app.api.v1.schemas.payment import PaymentProcessResponse, PaymentProcessRequest
from app.db.crud.movie import get_movie_session, update_movie_session_seats
from app.db.crud.payment import create_payment
from app.db.crud.user import create_ticket
from app.db.models.user import UserModel

router = APIRouter(prefix="/payment", tags=["main"])

# Імітація обробки платежа


@router.post("/", response_model=PaymentProcessResponse, response_model_exclude_none=True,
             operation_id="process_payment")
async def process_payment(request: PaymentProcessRequest, user: UserModel = Depends(get_auth_user)):
    session = await get_movie_session(request.session_id)

    if session :
        if max(request.seats) <= session.seats:
            seats_array = [] if session.seats_busy == "[]" else (
                list(map(int, session.seats_busy.strip("[]").split(", "))))

            if not bool(set(seats_array) & set(request.seats)):
                if len(request.card_number) == 16 and len(request.card_cvv) == 3:
                    seats_array.extend(request.seats)

                    await update_movie_session_seats(request.session_id, seats_array)

                    ticket_id = await create_ticket(user.id, request.session_id, request.seats)

                    await create_payment(user.id, ticket_id, request.card_number, request.card_name,
                                         session.film.price * len(request.seats))

                    return PaymentProcessResponse(success=True)
                else:
                    return PaymentProcessResponse(success=False,
                                                  message="pages.film.payment.payment.exception.invalid_card")
            else:
                return PaymentProcessResponse(success=False, message="pages.film.payment.exception.invalid_seats")
        else:
            return PaymentProcessResponse(success=False, message="pages.film.payment.exception.not_enough_seats")
    else:
        return PaymentProcessResponse(success=False, message="pages.film.payment.exception.session_not_found")
