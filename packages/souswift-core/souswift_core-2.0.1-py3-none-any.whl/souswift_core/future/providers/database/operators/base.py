import typing

from sqlalchemy.sql import ColumnCollection, ColumnElement, Select
from sqlalchemy.sql.elements import BooleanClauseList

from souswift_core.future.providers.database.types import Entity

ComparationOutput: typing.TypeAlias = (
    BooleanClauseList | ColumnElement[Boolean]
)
T = typing.TypeVar('T', contravariant=True)


class Filter(typing.Protocol):
    def __call__(
        self, entity_cls: type[Entity] | ColumnCollection
    ) -> ComparationOutput:
        ...


class Comparator(typing.Protocol[T]):
    def __call__(self, attr: ColumnElement, expected: T) -> ComparationOutput:
        ...


class Wrapper(typing.Protocol[T]):
    def __call__(self, val: T) -> typing.Any:
        ...


class OrderBy(typing.Protocol):
    def __call__(self, entity_cls: type[Entity], query: Select) -> Select:
        ...


class Paginate(typing.Protocol):
    def __call__(self, query: Select) -> Select:
        ...
