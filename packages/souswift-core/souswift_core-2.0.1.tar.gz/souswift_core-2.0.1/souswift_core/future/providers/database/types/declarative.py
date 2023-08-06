import typing

import sqlalchemy.orm as sa_orm
from sqlalchemy import MetaData

from souswift_core.future.providers.database.types import fields

T = typing.TypeVar('T')
P = typing.ParamSpec('P')


def __dataclass_transform__(
    *,
    eq_default: bool = True,
    order_default: bool = False,
    kw_only_default: bool = False,
    field_specifiers: tuple[type | typing.Callable[..., typing.Any], ...] = (),
) -> typing.Callable[[T], T]:
    return lambda a: a


def as_declarative(cls: type[T]) -> type[T]:
    return sa_orm.as_declarative()(cls)


_field_specifier = (
    fields.Field,
    fields.IntField,
    fields.FloatField,
    fields.DateTimeField,
    fields.DateField,
    fields.BooleanField,
    fields.TextField,
    fields.StringField,
    fields.ListField,
    fields.DictField,
    fields.JsonField,
)


@__dataclass_transform__(
    kw_only_default=True,
    field_specifiers=_field_specifier,
)
class MetaEntity(type):
    metadata: MetaData
