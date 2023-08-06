import typing

import pydantic
from pydantic.generics import GenericModel

from . import model

T = typing.TypeVar('T')
StrLike = typing.TypeVar('StrLike', bound=str)


class Details(model.Model):
    last_id: int | None = None
    total_pages: int | None = None
    info: str | None = None
    total_left: int | None = None


class BaseResponse(GenericModel, typing.Generic[T]):
    data: list[T]
    details: Details | None = pydantic.Field(default_factory=Details)


class BaseRequest(GenericModel, typing.Generic[T]):
    data: list[T]


class BaseError(GenericModel, typing.Generic[StrLike], model.Model):
    title: str
    path: str
    status: int
    detail: str
    error_key: StrLike | None = None
