import uvicorn
from fastapi import FastAPI
from sqlalchemy_utils import create_database, database_exists

from config.service import get_config
from database.client import DBClientManager
from router import router as apirouter

app = FastAPI()

config = get_config()
DB_URI = config.db.URI

if not database_exists(DB_URI):
    create_database(DB_URI)

database_client = DBClientManager(url=DB_URI)

database_client._registry.metadata.create_all(database_client._engine)

app.include_router(apirouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, log_level="debug")
