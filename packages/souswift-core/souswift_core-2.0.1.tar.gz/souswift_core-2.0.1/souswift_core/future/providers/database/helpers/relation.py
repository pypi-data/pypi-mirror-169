import functools
import typing
from types import FunctionType

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from souswift_core.future.providers.database.types import Entity

EntityT = typing.TypeVar('EntityT', bound=Entity)


def create_relation_table(table_name: str, *entities: str):
    return sa.Table(
        table_name,
        Entity.metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        *[
            sa.Column(
                f'{entity}_id', sa.Integer, sa.ForeignKey(f'{entity}.id')
            )
            for entity in entities
        ],
    )


@typing.overload
def make_relation(
    __relation__: None = None,
    /,
    *,
    name: str,
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: bool = False,
    secondary: sa.Table | None = None,
    foreign_keys: typing.Sequence[str] | None = None,
) -> typing.Any:
    ...


@typing.overload
def make_relation(
    __relation__: type[EntityT],
    /,
    *,
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: typing.Literal[False] = False,
    secondary: sa.Table | None = None,
    foreign_keys: typing.Sequence[str] | None = None,
) -> EntityT:
    ...


@typing.overload
def make_relation(
    __relation__: type[EntityT],
    /,
    *,
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: typing.Literal[True],
    secondary: sa.Table | None = None,
    foreign_keys: typing.Sequence[str] | None = None,
) -> list[EntityT]:
    ...


@typing.overload
def make_relation(
    __relation__: typing.Callable[[], type[EntityT]],
    /,
    *,
    name: str,
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: typing.Literal[False] = False,
    secondary: sa.Table | None = None,
    foreign_keys: typing.Sequence[str] | None = None,
) -> EntityT:
    ...


@typing.overload
def make_relation(
    __relation__: typing.Callable[[], type[EntityT]],
    /,
    *,
    name: str,
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: typing.Literal[True],
    secondary: sa.Table | None = None,
    foreign_keys: typing.Sequence[str] | None = None,
) -> list[EntityT]:
    ...


def make_relation(
    __relation__: (
        type[EntityT] | typing.Callable[[], type[EntityT]] | None
    ) = None,
    /,
    *,
    name: str = '',
    back_populates: str,
    lazy: str = 'selectin',
    __use_list__: bool = False,
    **kwargs,
) -> typing.Any:
    relation_func = functools.partial(
        relationship, back_populates=back_populates, lazy=lazy, **kwargs
    )
    if isinstance(__relation__, FunctionType) or __relation__ is None:
        return relation_func(argument=name)
    return relation_func(argument=__relation__.__qualname__)
