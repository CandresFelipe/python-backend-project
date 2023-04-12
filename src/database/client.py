from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


class DBClientManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self._engine: Engine = create_engine(self.url, echo=True)
        self._session = sessionmaker(bind=self._engine)

    @property
    def engine(self) -> Engine:
        return self._engine