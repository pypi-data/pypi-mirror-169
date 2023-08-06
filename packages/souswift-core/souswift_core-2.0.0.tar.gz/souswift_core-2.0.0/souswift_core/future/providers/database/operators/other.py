from typing import Literal

from sqlalchemy.sql import Select

from souswift_core.future.providers.database.types import Entity

from . import base, comp, where


def order_by_factory(
    field: str, order: Literal['asc', 'desc'] | None = None
) -> base.OrderBy:
    def order_by(entity_cls: type[Entity], query: Select) -> Select:
        if order is None:
            return query
        attr = where.retrieve_col_element(entity_cls, field)
        if order == 'asc':
            return query.order_by(attr.asc())
        return query.order_by(attr.desc())

    return order_by


null_order = order_by_factory('')


def limit_offset_paginate(limit: int, offset: int) -> base.Paginate:
    def paginate(query: Select) -> Select:
        return query.limit(limit).offset(offset)

    return paginate


def id_paginate(limit: int, last_id: int) -> base.Paginate:
    def paginate(query: Select) -> Select:
        return query.where(
            where.field_filter_factory('pk', last_id, comparator=comp.greater)(
                query.selected_columns
            )
        ).limit(limit)

    return paginate


def _null_paginate(limit: int, offset: int) -> base.Paginate:
    del limit, offset

    def paginate(query: Select) -> Select:
        return query

    return paginate


null_paginate = _null_paginate(0, 0)
