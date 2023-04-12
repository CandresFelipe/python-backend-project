from .base import BaseConfig


class Config(BaseConfig):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_URL: str
    DB_DATABASE: str
    DB_PORT: int
