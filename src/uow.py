from sqlalchemy.orm import Session

from database.client import DBClientManager


class SQLUnitOfWork:
    def __init__(self, db_connection: DBClientManager) -> None:
        self.db_connection = db_connection
        self.session = self.db_connection.session

    def __enter__(self) -> Session:
        return self.session.rollback()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
