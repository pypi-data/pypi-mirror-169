import typing
from datetime import date, datetime

import sqlalchemy as sa


class LongStr(str):
    """Only to diferentiate sa.String to sa.Text"""


_type_mapping = {
    str: sa.String,
    int: sa.Integer,
    float: sa.Float,
    datetime: sa.TIMESTAMP,
    date: sa.Date,
    bool: sa.Boolean,
    LongStr: sa.Text,
    list: sa.JSON,
    dict: sa.JSON,
}

_Types = str | int | float | datetime | date | bool | LongStr | list | dict

T = typing.TypeVar('T', bound=_Types)


def IntField(
    column: str | None = None,
    foreign_key: sa.ForeignKey | None = None,
    *,
    primary_key: bool = False,
    default: int | typing.Callable[[], int] | None = None,
    index: bool = False,
    nullable: bool = True,
    **kwargs,
) -> int:
    return Field(
        int,
        name=column,
        foreign_key=foreign_key,
        primary_key=primary_key,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def FloatField(
    precision: typing.Any = None,
    asdecimal: bool = False,
    decimal_return_scale: typing.Any = None,
    *,
    default: float | typing.Callable[[], float] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> float:
    return Field(
        float,
        precision,
        asdecimal,
        decimal_return_scale,
        name=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def DateTimeField(
    timezone: bool = False,
    *,
    default: datetime | typing.Callable[[], datetime] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> datetime:
    return Field(
        datetime,
        timezone,
        name=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def DateField(
    *,
    default: date | typing.Callable[[], date] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> date:
    return Field(
        date,
        name=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def BooleanField(
    *,
    default: bool | typing.Callable[[], bool] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> bool:
    return Field(
        bool,
        name=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def TextField(
    *,
    default: str | typing.Callable[[], str] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    foreign_key: sa.ForeignKey | None = None,
    **kwargs,
) -> str:
    return Field(
        LongStr,
        name=column,
        foreign_key=foreign_key,
        default=default,
        index=index,
        nullable=nullable,
        *kwargs,
    )


def StringField(
    length: int,
    collation: str | None = None,
    convert_unicode: bool = False,
    unicode_error: str | None = None,
    *,
    primary_key: bool = False,
    default: str | typing.Callable[[], str] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    foreign_key: sa.ForeignKey | None = None,
    **kwargs,
) -> str:
    return Field(
        str,
        length,
        collation,
        convert_unicode,
        unicode_error,
        primary_key=primary_key,
        name=column,
        foreign_key=foreign_key,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def ListField(
    none_as_null: bool = False,
    *,
    default: list | typing.Callable[[], list] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> list:
    return JsonField(
        none_as_null,
        column=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def DictField(
    none_as_null: bool = False,
    *,
    default: dict | typing.Callable[[], dict] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> dict:
    return JsonField(
        none_as_null,
        column=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def JsonField(
    none_as_null: bool = False,
    *,
    default: typing.Any | typing.Callable[[], typing.Any] | None = None,
    index: bool = False,
    nullable: bool = True,
    column: str | None = None,
    **kwargs,
) -> typing.Any:
    return Field(
        list,
        none_as_null,
        name=column,
        default=default,
        index=index,
        nullable=nullable,
        **kwargs,
    )


def Field(
    type_: type[T],
    *type_args,
    column: str | None = None,
    foreign_key: sa.ForeignKey | None = None,
    default: T | typing.Callable[[], T] | None = None,
    index: bool = False,
    nullable: bool = True,
    primary_key: bool = False,
    server_default: typing.Any = None,
    **kwargs,
) -> T:
    args = (column, _type_mapping[type_](*type_args), foreign_key)
    args = [item for item in args if item is not None]
    return sa.Column(  # type: ignore
        *args,
        default=default,
        index=index,
        nullable=nullable,
        primary_key=primary_key,
        server_default=server_default,
        **kwargs,
    )
