from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException

from app.api.v1.routers.login import get_auth_user
from app.api.v1.schemas.admin.admin import AdminStatsResponse, AdminUserRequest, AdminUserSetRequest
from app.api.v1.schemas.movie import MovieRequest, MovieAddRequest, MoviesSessionsAdminRequest, MovieSessionsResponse, \
    MovieSessionRequest, MovieSessionsAddRequest
from app.api.v1.schemas.payment import PaymentProcessResponse, PaymentProcessRequest
from app.api.v1.schemas.user import UserMeResponse
from app.db.crud.movie import get_movie_session, update_movie_session_seats, get_all_movies, get_movies_count, \
    get_active_sessions, get_movies_profit, delete_movie, create_movie, get_all_sessions, delete_session, create_session
from app.db.crud.payment import create_payment
from app.db.crud.user import create_ticket, get_users_count, get_tickets_count, get_all_users, set_user_admin
from app.db.models.movie import MovieModel, MovieSessionModel
from app.db.models.user import UserModel
from app.user.permission import UserPermissions

router = APIRouter(prefix="/admin", tags=["main"])


@router.get("/stats",
            response_model=AdminStatsResponse, response_model_exclude_none=True, operation_id="get_admin_stats")
async def get_admin_stats(user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        return AdminStatsResponse(
            users=await get_users_count(),
            films=await get_movies_count(),
            sessions=await get_active_sessions(),
            tickets_sell=await get_tickets_count(),
            month_money=await get_movies_profit(),
            week_money=await get_movies_profit(7),

        )
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/users", response_model=List[UserMeResponse], response_model_exclude_none=True,
             operation_id="get_users_admin")
async def get_users_admin(request: Optional[AdminUserRequest] = None, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        request = request if request else AdminUserRequest()

        users = await get_all_users(request.limit, request.offset)

        result = []

        for user in users:
            result.append(UserMeResponse(
                id=user.id,
                email=user.email,
                name=user.name,
                picture=user.picture,
                permission=str(user.permission),
                register_time=user.register_time,
            ))

        return result
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/users/set", operation_id="set_user_admin")
async def get_users_admin(request: AdminUserSetRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        await set_user_admin(request.id, request.admin)
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/films/delete", operation_id="delete_movie_admin")
async def film_delete_admin(request: MovieRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        await delete_movie(request.id)
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/films/add", operation_id="add_movie_admin")
async def film_add_admin(request: MovieAddRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        await create_movie(MovieModel(
            title=request.title,
            description=request.description,
            image=request.image,
            afisha_image=request.afisha_image,
            lang=request.lang,
            genre=request.genre,
            time=request.time,
            trailer=request.trailer,
            price=request.price
        ))
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/sessions", response_model=List[MovieSessionsResponse], response_model_exclude_none=True,
            operation_id="get_session_admin")
async def get_session_admin(request: MoviesSessionsAdminRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        sessions = await get_all_sessions(request.limit, request.offset)

        result = []

        for session in sessions:
            result.append(MovieSessionsResponse(
                id=session.id,
                film_id=session.film_id,
                date=session.date,
                seats=session.seats,
                seats_busy=session.seats_busy,
                create_time=session.create_time,
                update_time=session.update_time,
            ))

        return result
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/sessions/delete", operation_id="delete_session_admin")
async def delete_session_admin(request: MovieSessionRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        await delete_session(request.id)
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/sessions/add", operation_id="add_session_admin")
async def add_session_admin(request: MovieSessionsAddRequest, user: UserModel = Depends(get_auth_user)):
    if user.permission.has(UserPermissions.ADMIN):
        await create_session(MovieSessionModel(
            film_id=request.film_id,
            date=request.date,
            seats_busy="[]",
            seats=request.seats,
        ))
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
