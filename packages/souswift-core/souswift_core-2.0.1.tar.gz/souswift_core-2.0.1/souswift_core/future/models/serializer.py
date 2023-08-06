import abc
import typing
from datetime import date
from functools import lru_cache
from uuid import UUID

from souswift_core.future.exc.models import NotSerializableError

ConverterType = typing.Callable[[typing.Any], typing.Any]


def uuid_serializer(uuid: UUID):
    return str(uuid)


def date_serializer(dt: date):
    return str(dt)


class Serializable(abc.ABC):
    @abc.abstractmethod
    def serialize(self) -> typing.Any:
        ...

    @typing.final
    @staticmethod
    def parse(val: 'Serializable'):
        return val.serialize()


_SERIALIZER_MAPPING: dict[type, ConverterType] = {
    UUID: uuid_serializer,
    date: date_serializer,
    Serializable: Serializable.parse,
}


def _default_serializer(obj) -> typing.NoReturn:
    raise NotSerializableError(type(obj), obj)


def _get_serializer(typ: type) -> ConverterType:
    serializer = _SERIALIZER_MAPPING.get(typ) or _find_by_hierarchy(type)
    return serializer or _default_serializer


@lru_cache(maxsize=32)
def _find_by_hierarchy(typ: type) -> ConverterType | None:
    keys = set(_SERIALIZER_MAPPING)
    intersection = {val for val in keys if issubclass(typ, val)}
    return _get_serializer(intersection.pop())


def serializer(obj: typing.Any) -> typing.Any:
    _serializer = _get_serializer(type(obj))
    return _serializer(obj)
