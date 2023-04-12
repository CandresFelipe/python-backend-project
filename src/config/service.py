from .models import Config
from .models import DBConfig


def get_config() -> Config:
    """Read configuration from .env file

    Returns:
        Config: It returns a config instance
    """
    return Config(db=DBConfig())
