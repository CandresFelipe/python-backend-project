from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session as SQLSession
from sqlalchemy.exc import SQLAlchemyError

from contextlib import contextmanager


class DBClientManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self._engine: Engine = create_engine(self.url, echo=True)
        self._session = sessionmaker(bind=self._engine)

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def session(self) -> sessionmaker[SQLSession]:
        return self._session

    @contextmanager
    def managed_session(self) -> sessionmaker[SQLSession]:
        try:
            with self._session.begin() as session:
                yield session
        except SQLAlchemyError as error:
            print(error)

    @contextmanager
    def managed_engine(self) -> Engine:
        try:
            with self._engine.begin() as engine:
                yield engine
        except SQLAlchemyError as error:
            print(error)
