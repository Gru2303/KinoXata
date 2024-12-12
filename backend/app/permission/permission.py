import math

from typing import TypeVar, Generic
from enum import IntEnum


class PermissionsEnum(IntEnum):
    pass


T = TypeVar('T', bound=PermissionsEnum)


class Permissions(Generic[T]):
    def __init__(self, perm: str = None, size: int = 32):
        if size <= 0:
            raise ValueError("Size must be greater than 0")

        if perm :
            self._buffer = bytearray.fromhex(perm)
        else:
            self._buffer = bytearray(math.ceil(size / 8))

    def set(self, *flags: T):
        for flag in flags:
            if len(self._buffer) <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            self._buffer[flag.value // 8] |= 1 << flag.value

    def clear(self, *flags: T):
        for flag in flags:
            if len(self._buffer) <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            self._buffer[flag.value // 8] &= ~(1 << flag.value)

    def has(self, *flags: T):
        result = True

        for flag in flags:
            if len(self._buffer) <= flag.value:
                raise ValueError(f"Flag {flag} is out of range")

            if not self._buffer[flag.value // 8] & (1 << flag.value):
                result = False

                break

        return result

    def __str__(self):
        return self._buffer.hex()
