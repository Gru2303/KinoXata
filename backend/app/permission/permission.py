import math

from typing import TypeVar, Generic
from enum import IntEnum


class PermissionsEnum(IntEnum):
    pass


T = TypeVar('T', bound=PermissionsEnum)


class Permissions(Generic[T]):
    MAX_SIZE = 8
    DEFAULT_PERMISSIONS = "0000000000000000"

    def __init__(self, perm: str = None):
        if perm :
            self._buffer = bytearray.fromhex(perm)

            if len(self._buffer) < Permissions.MAX_SIZE:
                self._buffer.extend(bytearray(Permissions.MAX_SIZE - len(self._buffer)))
        else:
            self._buffer = bytearray(Permissions.MAX_SIZE)

    def set(self, *flags: T):
        for flag in flags:
            if len(self._buffer) * 8 <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            self._buffer[flag.value // 8] |= 1 << flag.value

    def clear(self, *flags: T):
        for flag in flags:
            if len(self._buffer) * 8 <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            self._buffer[flag.value // 8] &= ~(1 << flag.value)

    def has(self, *flags: T):
        result = True

        for flag in flags:
            if len(self._buffer) * 8 <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            if not self._buffer[flag.value // 8] & (1 << flag.value):
                result = False

                break

        return result

    def __len__(self):
        return len(self._buffer)

    def __str__(self):
        return self._buffer.hex()
