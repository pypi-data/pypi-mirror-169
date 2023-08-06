import typing

import pydantic
from pydantic import BaseModel, root_validator

from souswift_core.future.utils import string
from souswift_core.future.utils.helpers import lazy_field

from . import json, serializer

ModelT = typing.TypeVar('ModelT', bound='Model')


class Model(BaseModel, serializer.Serializable):
    """Classe padrão para representação de dados"""

    def serialize(self) -> typing.Any:
        return self.dict(by_alias=True)

    def raw_dict(self, by_alias: bool = True, exclude: set[str] | None = None):
        exclude = exclude or set()
        return json.loads(self.json(by_alias=by_alias, exclude=exclude))

    def clone(self, **fields):
        return self.parse_obj(dict(self) | fields)

    @lazy_field
    @classmethod
    def optional(cls: type[ModelT], exclude: tuple[str, ...]) -> ModelT:
        new_t = pydantic.create_model(
            f'Optional{cls.__name__}',
            __base__=type(  # type: ignore
                f'Optional{cls.__name__}',
                (cls, NotEmptyModel),
                dict(cls.__dict__),
            ),
        )
        for item in exclude:
            new_t.__fields__.pop(item, None)
        for field in new_t.__fields__.values():
            field.required = False
            field.allow_none = False
            field.default = None
        return new_t  # type: ignore

    class Config:
        json_loads = json.loads
        json_dumps = json.dumps
        frozen = True
        allow_population_by_field_name = True
        alias_generator = string.to_camel


class NotEmptyModel(Model):
    """NotEmptyModel representa dados que precisam de ao menos um valor válido"""

    @root_validator
    @classmethod
    def model_should_not_be_empty(cls, values: typing.Mapping):
        if all(value is None for value in values.values()):
            raise ValueError(
                f'Object {cls.__name__} must have at least one field valid'
            )
        return values


class UnsafeModel(Model):
    """UnsafeModel remove imutabilidade do model padrão"""

    class Config(Model.Config):
        frozen = False
