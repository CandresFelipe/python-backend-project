from sqlalchemy import URL, Column, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy_utils import generic_repr

from database.sql_base import SQLAlchemyDeclarativeBase


@generic_repr
class Item(SQLAlchemyDeclarativeBase):
    __tablename__ = "item"
    id: Mapped[int] = Column(Integer, primary_key=True)
    uuid: Mapped[str] = Column(String, nullable=False, unique=True)
    name: Mapped[str] = Column(String, nullable=False)
    description: Mapped[str] = Column(String, nullable=False)
    size: Mapped[str] = Column(String(1), nullable=True)
    color: Mapped[str] = Column(String, nullable=False)
    image_url: Mapped[URL] = Column(String, nullable=False)
    price: Mapped[str] = Column(String, nullable=False)
    locale_currency: Mapped[str] = Column(String, nullable=False)
