from typing import Any, Dict

from pydantic import PostgresDsn, validator

from .base import BaseConfig


class DBConfig(BaseConfig):
    """A class that describes a db object formed from the environment
        variable belonged to postgres info.

    Returns:
        string: it builds an `URI` object from database environment variable
    """

    class Config:
        env_prefix = "DB_"

    USERNAME: str
    PASSWORD: str
    URL: str
    DATABASE: str
    PORT: int = 5432
    URI: str = ""

    @validator("URI")
    def set_uri(v: str, values: Dict[str, Any]) -> str:
        uri: str = PostgresDsn.build(
            scheme="postgresql",
            user=values["USERNAME"],
            password=values["PASSWORD"],
            host=values["URL"],
            port=str(values["PORT"]),
            path=f"/{values['DATABASE']}",
        )
        return uri


class Config(BaseConfig):
    db: DBConfig
