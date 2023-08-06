import sqlalchemy.orm as sa_orm

from souswift_core.future.providers.database.types import fields


class SerialIdMixin:
    @sa_orm.declared_attr
    def id_(self):
        return fields.IntField('id', primary_key=True)


class DefaultMixin(SerialIdMixin):
    ...
