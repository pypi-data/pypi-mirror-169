import typing

from fastapi import FastAPI, Request, Response
from starlette.datastructures import State

from souswift_core.future.providers.database import config, provider
from souswift_core.future.utils.helpers import async_lazy_field, lazy_field


class DatabaseApiHandler:
    state_name = 'database_provider'

    def __init__(
        self,
        db_config: config.DatabaseConfig,
    ) -> None:
        self._config = db_config
        self._initialized = False

    @property
    def db_config(self):
        return self._config

    @db_config.setter
    def db_config(self, value: config.DatabaseConfig):
        if not self._initialized:
            self._config = value

    @property
    @lazy_field
    def _provider(self) -> provider.DatabaseProvider:
        return provider.DatabaseProvider(self.db_config)

    async def setup(self, state: State):
        self._initialized = True
        if hasattr(state, self.state_name):
            return
        setattr(state, self.state_name, self._provider)
        await self._provider.healthcheck()

    @classmethod
    def get(cls, request: Request) -> provider.DatabaseProvider:
        return getattr(request.app.state, cls.state_name)


class DatabaseDependency:
    def __init__(self, request: Request) -> None:
        self._provider = DatabaseApiHandler.get(request)

    def context(self):
        return self._provider.context()


class RequestDatabaseContext:
    state_name = 'database_context'

    def __init__(self, request: Request) -> None:
        self._provider = DatabaseApiHandler.get(request)
        self._request = request

    @async_lazy_field
    async def context(self):
        context = self._provider.context()
        setattr(self._request.state, self.state_name, context)
        return await context

    @classmethod
    def setup_cleanup_middleware(cls, app: FastAPI) -> None:
        @app.middleware('http')
        async def _(
            request: Request,
            call_next: typing.Callable[
                [Request], typing.Coroutine[typing.Any, typing.Any, Response]
            ],
        ):
            response = await call_next(request)
            if context := getattr(request.state, cls.state_name, None):
                context: provider.DatabaseContext
                await context.finish()

            return response


def setup_database(app: FastAPI, db_config: config.DatabaseConfig):
    @app.on_event('startup')
    async def _():
        await DatabaseApiHandler(db_config).setup(app.state)

    RequestDatabaseContext.setup_cleanup_middleware(app)
