from database.client import DBClientManager
from sqlalchemy_utils import create_database, database_exists
from config.service import get_config

from sqlalchemy import URL


config = get_config()

URL_ENV = URL.create(
    drivername="postgresql",
    username=config.DB_USERNAME,
    password=config.DB_PASSWORD,
    host=config.DB_URL,
    port=config.DB_PORT,
    database=config.DB_DATABASE,
)

if URL_ENV != "":
    if not database_exists(URL_ENV):
        create_database(URL_ENV)
    db = DBClientManager(URL_ENV)
    print(db._engine.url)
else:
    print("url not found")
