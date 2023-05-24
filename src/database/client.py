import contextlib
import importlib
from typing import Iterator, NoReturn

from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from config.models import DBConfig
from database.type import mapper_registry


class DBClientManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self._engine: Engine = create_engine(self.url, echo=True)
        self._session = sessionmaker(autocommit=False, bind=self._engine)
        self._registry = mapper_registry

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def session(self) -> Session:
        return self._session

    @classmethod
    def get_from_config(cls, config: DBConfig):
        return cls(url=config.URI)

    @contextlib.contextmanager
    def managed_session(self) -> Iterator[Session]:
        try:
            with self._session.begin() as session:
                print("entering session...")
            yield session
            print("leaving session ...")
        except SQLAlchemyError as err:
            self._exc_raise(err)

    def _exc_raise(self, exc: Exception) -> NoReturn:
        raise print(f"Encountered SQLAlchemyError : {exc}") from exc

    def shutdown(self) -> None:
        print("stopping database connection...")
        self._engine.dispose()

    def create_or_update_models(self) -> None:
        inspector = inspect(self._engine)
        existing_tables = inspector.get_table_names()

        models_module = importlib.import_module("database.models")

        for model_name in models_module.__all__:
            model = getattr(models_module, model_name)
            table_name = model.__tablename__

            if table_name not in existing_tables:
                self._registry.metadata.tables[table_name].create(bind=self._engine)
