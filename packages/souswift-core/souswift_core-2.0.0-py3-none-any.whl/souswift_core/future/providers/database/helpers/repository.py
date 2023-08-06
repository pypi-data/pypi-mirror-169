import typing

import sqlalchemy as sa

from souswift_core.future.exc.helpers import async_raise_on_none
from souswift_core.future.providers.database import DatabaseContext, operators, types

EntityT = typing.TypeVar('EntityT', bound=types.Entity)


def make_selector(entity_cls: type[EntityT]):
    query = sa.select(entity_cls)

    async def select(
        context: DatabaseContext,
        *where: operators.Filter,
        order_by: operators.OrderBy = operators.null_order,
        paginate: operators.Paginate = operators.null_paginate
    ) -> list[EntityT]:
        select_q = query.where(
            operators.join_filters_factory(where)(entity_cls)
        )
        select_q = paginate(order_by(entity_cls, select_q))
        async with context:
            async with context.session as session:
                result = await session.execute(select_q)
                return result.scalars().all()

    return select


def make_getter(entity_cls: type[EntityT]):
    query = sa.select(entity_cls)

    @async_raise_on_none(entity_cls.__name__)
    async def get(
        context: DatabaseContext, where: operators.Filter
    ) -> EntityT | None:
        get_q = query.where(where(entity_cls))
        async with context:
            async with context.session as session:
                result = await session.execute(get_q)
                return result.scalars().first()

    return get


def make_creator(entity_cls: type[EntityT]):
    async def create(
        context: DatabaseContext, payload: dict[str, typing.Any]
    ) -> EntityT:
        async with context:
            async with context.session as session:
                entity = entity_cls(**payload)
                session.add(entity)
                await session.flush([entity])
                return entity

    return create


def make_updater(entity_cls: type[EntityT]):
    inner_getter = make_getter(entity_cls)

    async def update(
        context: DatabaseContext,
        payload: dict[str, typing.Any],
        where: operators.Filter,
    ) -> EntityT:
        async with context:
            async with context.session as session:
                entity = await inner_getter(context, where)
                entity.set(**payload)
                session.add(entity)
                await session.flush([entity])
                return entity

    return update


def make_deleter(entity_cls: type[types.Entity]):
    inner_getter = make_getter(entity_cls)

    async def delete(context: DatabaseContext, where: operators.Filter):
        async with context:
            async with context.session as session:
                entity = await inner_getter(context, where)
                await session.delete(entity)
                await session.flush()

    return delete
