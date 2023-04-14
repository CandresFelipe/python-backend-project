from database.base import SQLAlchemyDeclarativeBase
from sqlalchemy import Column, String, URL, Integer

from sqlalchemy.orm import Mapped


class Item(SQLAlchemyDeclarativeBase):
    __tablename__ = "product"

    uuid: Mapped[str] = Column(String, nullable=False, unique=True)
    name: Mapped[str] = Column(String, nullable=False)
    description: Mapped[str] = Column(String, nullable=False)
    size: Mapped[str] = Column(String(1), nullable=True)
    color: Mapped[str] = Column(String, nullable=False)
    image_uri: Mapped[URL] = Column(String, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    locale_currency: Mapped[str] = Column(Integer, nullable=False)
