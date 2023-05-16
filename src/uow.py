from abc import abstractmethod
from types import TracebackType
from typing import Protocol, TypeVar

from sqlalchemy.orm import Session

from database.type import Sessionmaker

T = TypeVar("T")


class AbstractSQLUnitOfWork(Protocol[T]):
    repo: T

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        ...

    @abstractmethod
    def rollback(self) -> None:
        ...

    @abstractmethod
    def commit(self) -> None:
        ...


# This class helps to handle multiple session from a db connection


class Repo(Protocol):
    def __init__(self, session: Session) -> None:
        ...


RT = TypeVar("RT", bound=Repo)


class SQLUnitOfWork(AbstractSQLUnitOfWork[RT]):
    def __init__(self, repo_cls: type[RT], sessionmaker: Sessionmaker) -> None:
        self.repo_cls = repo_cls
        self.sessionmaker = sessionmaker

    def __enter__(self):
        self.session = self.sessionmaker()
        self.repo = self.repo_cls(self.session)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.session.close()

    def rollback(self) -> None:
        return self.session.rollback()

    def commit(self) -> None:
        self.session.commit()
