import typing

from .base import SouSwiftCoreError


class NotSerializableError(SouSwiftCoreError):
    def __init__(self, type_: type, val: typing.Any) -> None:
        super().__init__(f'Object {val} of type {type_} is not serializable')
        self.type_ = type_
        self.val = val
