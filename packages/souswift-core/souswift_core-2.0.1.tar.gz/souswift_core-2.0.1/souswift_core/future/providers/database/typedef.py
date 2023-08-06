import enum
import typing

import sqlalchemy.pool as sa_pool

from souswift_core.future import enums


class DriverTypes(typing.Protocol):
    port: int
    async_driver: str
    sync_driver: str
    required_fields: list[str]
    config: dict[str, typing.Any]
    timeout_arg_name: str


class MysqlDriver:
    port = 3306
    async_driver = 'mysql+aiomysql'
    sync_driver = 'mysql+pymysql'
    required_fields = ['user', 'password', 'host', 'port', 'name']
    config = {}
    timeout_arg_name = 'connect_timeout'


class SqliteDriver:
    port = 0
    async_driver = 'sqlite+aiosqlite'
    sync_driver = 'sqlite'
    required_fields = ['host']
    config = {
        'connect_args': {'check_same_thread': False},
        'poolclass': sa_pool.StaticPool,
    }
    timeout_arg_name = 'timeout'


class Driver(enums.StrEnum):
    MYSQL = enum.auto()
    SQLITE = enum.auto()


MYSQL = Driver.MYSQL
SQLITE = Driver.SQLITE

DRIVER_MAPPING: dict[Driver, DriverTypes] = {
    MYSQL: MysqlDriver(),
    SQLITE: SqliteDriver(),
}

IterableToDict = typing.Iterable[tuple[typing.Any, typing.Any]]


class SupportsKeyAndGetItem(typing.Protocol):
    def keys(self) -> typing.Iterable[typing.Any]:
        ...

    def __getitem__(self, __k: typing.Any) -> typing.Any:
        ...


DictConvertable = IterableToDict | SupportsKeyAndGetItem
