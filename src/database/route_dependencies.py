from config.service import get_config
from database.client import DBClientManager
from database.type import Sessionmaker


def get_db_sessionmaker() -> Sessionmaker:
    config = get_config()
    db = DBClientManager(url=config.db.URI)
    return db._session
