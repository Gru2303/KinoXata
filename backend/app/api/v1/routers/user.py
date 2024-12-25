from typing import Any, Coroutine, List

from fastapi import APIRouter, Depends
from select import select
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from app.api.v1.routers.login import get_auth_user
from app.api.v1.schemas.movie import MovieResponse
from app.api.v1.schemas.user import UserMeResponse, UserTicketResponse, UserTicketSignRequest
from app.db.crud.token import verify_token, deactivate_token
from app.db.crud.user import get_all_tickets, get_ticket_by_sign
from app.db.models.movie import MovieModel
from app.db.models.user import UserModel, UserTicketModel
from app.user.permission import UserPermissions

router = APIRouter(prefix="/user", tags=["main"])


@router.get("/me",
            response_model=UserMeResponse,
            response_model_exclude_none=True,
            operation_id="get_user_me")
async def me(user: UserModel = Depends(get_auth_user)):
    return UserMeResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        picture=user.picture,
        permission=str(user.permission),
        register_time=user.register_time,
    )


@router.get("/tickets",
            response_model=List[UserTicketResponse],
            response_model_exclude_none=True,
            operation_id="get_tickets")
async def get_tickets(user: UserModel = Depends(get_auth_user)):
    tickets = await get_all_tickets(user.id)

    result: List[UserTicketResponse] = []

    for i in tickets:
        seats_array = list(map(int, i.seats_busy.strip("[]").split(", ")))

        film = i.session.film

        result.append(UserTicketResponse(
            id=i.id,
            film=MovieResponse(
                id=film.id,
                title=film.title,
                description=film.description,
                image=film.image,
                afisha_image=film.afisha_image,
                lang=film.lang,
                genre=film.genre,
                time=film.time,
                trailer=film.trailer,
                price=film.price,
                create_time=film.create_time,
                update_time=film.update_time
            ),
            seats=seats_array,
            date=i.session.date,
            secret=i.secret,
        ))

    return result


@router.post("/ticket/sign",
             response_model=UserTicketResponse,
             response_model_exclude_none=True,
             operation_id="get_ticket_by_sign")
async def get_ticket_by_sign_request(request: UserTicketSignRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        result = await get_ticket_by_sign(request.sign)

        if result:
            seats_array = [] if result.seats_busy == "[]" else (
                list(map(int, result.seats_busy.strip("[]").split(", "))))
            film = result.session.film

            return UserTicketResponse(
                id=result.id,
                film=MovieResponse(
                    id=film.id,
                    title=film.title,
                    description=film.description,
                    image=film.image,
                    afisha_image=film.afisha_image,
                    lang=film.lang,
                    genre=film.genre,
                    time=film.time,
                    trailer=film.trailer,
                    price=film.price,
                    create_time=film.create_time,
                    update_time=film.update_time
                ),
                seats=seats_array,
                date=result.session.date,
                secret=result.secret,
            )
        else:
            raise HTTPException(status_code=404, detail="Ticket not found")

    raise HTTPException(status_code=403, detail="Forbidden")
