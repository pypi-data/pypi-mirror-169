import typing
from inspect import isclass

import sqlalchemy as sa
from sqlalchemy.sql import ColumnCollection, ColumnElement

from souswift_core.future.providers.database.types import Entity

from . import base, comp, wrap

T = typing.TypeVar('T')

FilterParamType = type[Entity] | ColumnCollection


def field_filter_factory(
    field: str,
    expected: T,
    comparator: base.Comparator[T] = comp.equals,
    wrapper: base.Wrapper[T] = wrap.default_wrapper,
) -> base.Filter:
    def field_filter(entity_cls: FilterParamType) -> base.ComparationOutput:
        col_element = retrieve_col_element(entity_cls, field)
        if expected is None:
            return sa.true()
        return comparator(col_element, wrapper(expected))

    return field_filter


def and_filter_factory(*filters: base.Filter) -> base.Filter:
    def and_filter(entity_cls: FilterParamType) -> base.ComparationOutput:
        return sa.and_(*(f(entity_cls) for f in filters))

    return and_filter


def or_filter_factory(*filters: base.Filter) -> base.Filter:
    def or_filter(entity_cls: FilterParamType) -> base.ComparationOutput:
        return sa.or_(*(f(entity_cls) for f in filters))

    return or_filter


def join_filters_factory(filters: typing.Sequence[base.Filter]) -> base.Filter:
    return and_filter_factory(*filters)


def retrieve_col_element(entity: FilterParamType, field: str) -> ColumnElement:
    if isclass(entity) and issubclass(entity, Entity):
        field = 'id_' if field == 'pk' else field
    return getattr(entity, field)
