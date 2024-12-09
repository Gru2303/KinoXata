import uvicorn

from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from db import session

from api import v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    await session.create_tables()

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)