import typing

import pydantic
import sqlalchemy.engine as sa_engine

from souswift_core.future.config import MissingNamesError
from souswift_core.future.providers import config
from souswift_core.future.utils.helpers import lazy_field

from . import typedef


class DatabaseConfig(config.ProviderConfig):
    _prefix_ = 'db'

    driver: typedef.Driver
    host: str
    name: str = ''
    user: str = ''
    password: str = ''
    port: int = 0
    pool_size: int = 20
    pool_recycle: int = 3600
    max_overflow: int = 0
    connect_timeout: float = -1

    @pydantic.root_validator
    @classmethod
    def validate_fields_received(cls, values: typing.Mapping[str, typing.Any]):
        driver: typedef.Driver = values['driver']
        driver_type = typedef.DRIVER_MAPPING[driver]
        sentinel = object()
        received_fields = {
            item: values.get(item, sentinel)
            for item in driver_type.required_fields
        }
        if (
            received_fields.get('port')
            and 'port' in driver_type.required_fields
        ):
            received_fields['port'] = driver_type.port
        if missing_names := [
            name
            for name, value in received_fields.items()
            if value is sentinel
        ]:
            raise MissingNamesError(*missing_names)
        return values

    @property
    @lazy_field
    def timeout_config(self):
        return (
            {
                'connect_args': {
                    self.driver_type.timeout_arg_name: self.connect_timeout
                }
            }
            if self.connect_timeout
            else {}
        )

    @property
    @lazy_field
    def driver_type(self):
        return typedef.DRIVER_MAPPING[self.driver]

    @property
    @lazy_field
    def parsed_port(self):
        return self.port or self.driver_type.port

    @property
    @lazy_field
    def pool_config(self):
        driver_type = self.driver_type
        return driver_type.config or {
            'pool_size': self.pool_size,
            'pool_recycle': self.pool_recycle,
            'max_overflow': self.max_overflow,
        }


def _uri_maker_factory(is_async: bool):
    def make_uri(config: DatabaseConfig):
        driver_type = config.driver_type
        drivername = (
            driver_type.async_driver if is_async else driver_type.sync_driver
        )
        if config.driver is typedef.SQLITE:
            return sa_engine.URL.create(
                drivername=drivername, database=config.host
            )
        return sa_engine.URL.create(
            drivername=drivername,
            username=config.user,
            password=config.password,
            host=config.host,
            port=config.parsed_port,
            database=config.name,
        )

    return make_uri


make_sync_uri = _uri_maker_factory(is_async=False)
make_async_uri = _uri_maker_factory(is_async=True)


def test_config_factory(host: str = ':memory:'):
    return DatabaseConfig(driver=typedef.SQLITE, host=host)
