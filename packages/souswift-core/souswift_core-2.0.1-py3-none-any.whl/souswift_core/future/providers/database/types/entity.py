import sqlalchemy.orm as sa_orm
from sqlalchemy import inspect
from sqlalchemy.orm.properties import ColumnProperty

from souswift_core.future.utils import string

from .declarative import as_declarative


@as_declarative
class Entity:
    @classmethod
    @sa_orm.declared_attr
    def __tablename__(cls):
        return string.to_snake(cls.__name__)

    @classmethod
    def _fields(cls):
        for prop in inspect(cls).iterate_properties:
            if isinstance(prop, ColumnProperty):
                yield prop.key

    def __iter__(self):
        for key in self._fields():
            yield key, getattr(self, key)

    def dict(self):
        return dict(self)

    def set(self, **vals):
        for key, val in vals.items():
            setattr(self, key, val)
