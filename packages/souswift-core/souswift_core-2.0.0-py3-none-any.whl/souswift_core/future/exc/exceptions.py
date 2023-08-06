import abc
import typing
from http import HTTPStatus

from .base import SouSwiftCoreError
from .types import ValidationPayload


def _append_exclamation_mark(message: str) -> str:
    return f'{message.removeprefix("!")}!'


class Error(SouSwiftCoreError):
    """`Error` is the base for
    all handled by api errors"""

    def __init__(
        self,
        message: str,
        status: HTTPStatus = HTTPStatus.BAD_REQUEST,
    ):
        super().__init__(message, status)
        self._message = message
        self._status = status

    @property
    def message(self) -> str:
        return _append_exclamation_mark(self._message)

    @property
    def status(self) -> HTTPStatus:
        return self._status


class ValidationError(Error):
    """`ValidationError` is the base for all validation errors"""

    def __init__(
        self, type_: str, field: str, detail: str, key: str | None = None
    ):
        super().__init__(detail, HTTPStatus.UNPROCESSABLE_ENTITY)
        self._type = type_
        self._field = field
        self._detail = detail
        self._key = key

    @property
    def payload(self) -> ValidationPayload:
        return {
            'type_': self._type,
            'field': self._field,
            'detail': self._detail,
            'error_key': self._key,
        }


class TargetError(Error, abc.ABC):
    """`TargetError` is a error with the same message only different target"""

    @typing.final
    def __init__(self, target: str) -> None:
        super().__init__(self.make_message(target), self.get_status())
        self._target = target

    @abc.abstractmethod
    def make_message(self, target: str) -> str:
        ...

    @abc.abstractmethod
    def get_status(self) -> HTTPStatus:
        ...


class NotFoundError(TargetError):
    def make_message(self, target: str) -> str:
        return f'{target} not found'

    def get_status(self) -> HTTPStatus:
        return HTTPStatus.NOT_FOUND


class ConflictError(TargetError):
    def make_message(self, target: str) -> str:
        return f'{target} already exists'

    def get_status(self) -> HTTPStatus:
        return HTTPStatus.CONFLICT


class ForbiddenError(TargetError):
    def make_message(self, target: str) -> str:
        return f'No permission to use {target}'

    def get_status(self) -> HTTPStatus:
        return HTTPStatus.FORBIDDEN


class UnauthorizedError(Error):
    def __init__(self, message: str):
        super().__init__(message, HTTPStatus.UNAUTHORIZED)


class UnexpectedError(Error):
    def __init__(
        self,
        message: str,
        status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
    ):
        super().__init__(message, status)


class UnavailableResourceError(Error):
    def __init__(
        self, message: str, status: HTTPStatus = HTTPStatus.SERVICE_UNAVAILABLE
    ):
        super().__init__(message, status)
