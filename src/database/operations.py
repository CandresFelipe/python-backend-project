from pathlib import Path
from alembic.config import Config
from alembic import command as alembic_command

BASE_DIR = Path(__name__).resolve().parent

ALEMBIC_INIT_PATH = BASE_DIR / "src" / "database" / "alembic.ini"


def run_migrations(url: str) -> None:
    """It creates migrations by setting the database url."""
    if not ALEMBIC_INIT_PATH.exists():
        raise FileNotFoundError("Alembic init file doesn't exist")
    alembic_config = Config(ALEMBIC_INIT_PATH)
    alembic_config.set_main_option("sqlalchemy.url", url)
    alembic_command.upgrade(alembic_config, "head")
