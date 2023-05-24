import sys

from pydantic import ValidationError

from .models import Config, DBConfig


def get_config() -> Config:
    """Read configuration from .env file

    Returns:
        Config: It returns a config instance
    """
    try:
        return Config(db=DBConfig())
    except ValidationError as exc:
        f"Application configuration error: {exc.errors()}"
        sys.exit(1)
