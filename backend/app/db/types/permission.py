from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import TypeDecorator

from app.permission import Permissions


class PermissionsType(TypeDecorator):
    impl = String

    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        if isinstance(value, Permissions):
            return str(value)

        raise ValueError("Unsupported type for CustomClassType")

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        return Permissions(value)
