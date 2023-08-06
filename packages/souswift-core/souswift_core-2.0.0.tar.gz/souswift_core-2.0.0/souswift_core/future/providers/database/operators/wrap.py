import typing
from datetime import date
from enum import Enum
from functools import lru_cache
from uuid import UUID

import sqlalchemy as sa

from . import base

T = typing.TypeVar('T')


def date_wrapper(val: str | date) -> typing.Any:
    return sa.func.date(val)


def null_wrapper(val: typing.Any):
    return val


def enum_wrapper(val: Enum):
    return val.value


def enum_name_wrapper(val: Enum):
    return val.name


def uuid_wrapper(val: UUID | str):
    return UUID(val) if isinstance(val, str) else val


class IntImpl(typing.Protocol):
    def __int__(self) -> ...:
        ...


def int_wrapper(val: IntImpl) -> typing.Any:
    return int(val)


def bool_wrapper(val: bool) -> typing.Any:
    return sa.true() if val else sa.false()


_default_mapping: dict[type, base.Wrapper] = {
    bool: bool_wrapper,
    Enum: enum_name_wrapper,
}


@lru_cache(maxsize=32)
def _find_by_intersection(typ: type):
    keys = set(_default_mapping)
    intersection = {val for val in keys if issubclass(typ, val)}
    if not intersection:
        return None
    return _get_wrapper(intersection.pop())


def _get_wrapper(typ: type):
    wrapper = _default_mapping.get(typ)
    if wrapper is None:
        wrapper = _find_by_intersection(typ)
    return wrapper or null_wrapper


def default_wrapper(val: typing.Any):
    wrapper = _get_wrapper(type(val))
    return wrapper(val)
