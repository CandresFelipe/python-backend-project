from fastapi import Depends

from database.route_dependencies import get_db_sessionmaker
from database.type import Sessionmaker
from uow import AbstractSQLUnitOfWork, SQLUnitOfWork

from .repository import ItemRepository


def get_db_session(
    sessionmaker: Sessionmaker = Depends(get_db_sessionmaker),
) -> AbstractSQLUnitOfWork[ItemRepository]:
    return SQLUnitOfWork(ItemRepository, sessionmaker)
