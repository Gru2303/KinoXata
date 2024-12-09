from enum import Enum

from fastapi import HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse


class ErrorResponse(BaseModel):
    message: str


class ErrorResponseEnum(Enum):
    @property
    def code(self):
        return self.value[0]

    @property
    def message(self):
        return self.value[1]

    @classmethod
    def responses(cls):
        return {error.code: {"model": ErrorResponse, "description": error.message} for error in cls}

    def response(self):
        return JSONResponse(status_code=self.code, content=ErrorResponse(message=self.message).model_dump())

    def exception(self):
        return HTTPException(status_code=self.code, detail=self.message)