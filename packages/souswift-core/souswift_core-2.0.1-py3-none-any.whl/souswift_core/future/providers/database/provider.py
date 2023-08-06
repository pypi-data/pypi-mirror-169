import typing
from contextlib import asynccontextmanager
from typing import Literal

import sqlalchemy.ext.asyncio as sa_asyncio
import sqlalchemy.future.engine as sa_engine
import sqlalchemy.orm as sa_orm

from souswift_core.future import exc
from souswift_core.future.providers.config import from_env
from souswift_core.future.utils import helpers

from .config import DatabaseConfig, make_async_uri


class DatabaseProvider:
    def __init__(self, config: DatabaseConfig | None = None):
        self._config = config or from_env(DatabaseConfig)

    @property
    def config(self):
        return self._config

    @property
    @helpers.lazy_field
    def engine(self):
        return sa_asyncio.create_async_engine(
            make_async_uri(self.config),
            **helpers.merge_dicts(
                self.config.pool_config, self.config.timeout_config
            ),
        )

    async def healthcheck(self, should_raise: bool = True):
        try:
            conn = await self.connect()
        except Exception as err:
            if should_raise:
                raise exc.UnavailableResourceError(
                    'Could not connect to database'
                ) from err
            return False
        else:
            await conn.close()
            return True

    def connect(self):
        return self.engine.connect()

    def context(self, context_class: type['DatabaseContext'] | None = None):
        context_class = context_class or DatabaseContext
        return context_class(self)


class DatabaseContext:
    def __init__(self, provider: DatabaseProvider) -> None:
        self._provider = provider
        self._online_contexts = 0

    @typing.overload
    def new(self, option: Literal['session']) -> sa_asyncio.AsyncSession:
        ...

    @typing.overload
    def new(self, option: Literal['connection']) -> sa_asyncio.AsyncConnection:
        ...

    def new(
        self, option: Literal['session', 'connection']
    ) -> sa_asyncio.AsyncConnection | sa_asyncio.AsyncSession:
        return (
            self._new_connection()
            if option == 'connection'
            else self._new_session()
        )

    def _new_connection(self):
        return self._provider.connect()

    def _new_session(self):
        return self._session_factory(self._new_connection())()

    @property
    @helpers.lazy_field
    def connection(self):
        return self._new_connection()

    @property
    @helpers.lazy_field
    def session(self):
        return self._session_factory(self.connection)()

    def _session_factory(
        self, conn: sa_asyncio.AsyncConnection
    ) -> 'sa_orm.sessionmaker[sa_asyncio.AsyncSession]':  # type: ignore
        return sa_orm.sessionmaker(
            conn,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
            class_=sa_asyncio.AsyncSession,  # type: ignore
        )

    def connect_from_sync(self, conn: sa_engine.Connection):
        async_connection = sa_asyncio.AsyncConnection(
            self._provider.engine, conn
        )
        helpers.update_field(
            self, async_connection, DatabaseContext.connection.fget
        )

    async def start(self):
        if not self._online_contexts:
            await self.connection
        self._online_contexts += 1

    async def finish(self):
        self._online_contexts -= 1
        if not self._online_contexts:
            await self.connection.close()
            helpers.reset_field(self, DatabaseContext.session.fget)
            helpers.reset_field(self, DatabaseContext.connection.fget)

    @property
    def is_active(self):
        return self._online_contexts > 0

    def __bool__(self):
        return self.is_active

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, *_):
        await self.finish()

    async def _start_self(self):
        await self.start()
        return self

    def __await__(self):
        return self._start_self().__await__()

    @asynccontextmanager
    async def acquire_connection(self):
        async with self:
            yield self.connection

    @asynccontextmanager
    async def acquire_session(self):
        async with self:
            async with self.session as session:
                yield session


class ConnectionContext(DatabaseContext):
    async def __aenter__(self):
        await super().__aenter__()
        return self.connection


class SessionContext(DatabaseContext):
    async def __aenter__(self):
        await super().__aenter__()
        return self.session
