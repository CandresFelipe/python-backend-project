from sqlalchemy_utils import create_database, database_exists

from config.service import get_config
from database.client import DBClientManager
from uow import SQLUnitOfWork

config = get_config()

DB_URI = config.db.URI

if not database_exists(DB_URI):
    create_database(DB_URI)

db = DBClientManager(DB_URI)
uow = SQLUnitOfWork(db)
print(f"started connection to uri {uow.db_connection._engine.url}")
