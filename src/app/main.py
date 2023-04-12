from database.client import DBClientManager
from sqlalchemy_utils import create_database, database_exists
from config.service import get_config


config = get_config()

DB_URI = config.db.URI

if not database_exists(DB_URI):
    create_database(DB_URI)

db = DBClientManager(DB_URI)
print(f"started connection to uri {db._engine.url}")
