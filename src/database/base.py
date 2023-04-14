from sqlalchemy import Column, Integer
from sqlalchemy.orm import declared_attr, Mapped
from .types import mapper_registry

# I use declarative mapping with decorators following this doc
# https://docs.sqlalchemy.org/en/14/orm/mapping_api.html#sqlalchemy.orm.registry.as_declarative_base


@mapper_registry.as_declarative_base()
class SQLAlchemyDeclarativeBase(object):

    """This class helps to apply declarative mapping process to all subclasses
    that derivates from it"""

    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> Mapped[str]:
        return cls.__tablename__.upper()
