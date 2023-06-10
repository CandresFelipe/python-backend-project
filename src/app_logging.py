import logging
import sys

from typing import Dict, Any
from loguru import logger
from config.service import get_config


# https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/#uvicorn-only-version
class InterceptHandler(logging.Handler):
    def emit(self, record):
        # get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # find caller from where originated the logged message
        frame, depth = sys._getframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def logging_config() -> Dict[str, Any]:
    config = get_config()
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {"class": "app_logging.InterceptHandler"},
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["console"],
                "level": config.LOG_LEVEL,
                "propagate": False,
            },
            "alembic": {
                "handlers": ["console"],
                "level": config.LOG_LEVEL,
                "propagate": False,
            },
            "sqlalchemy": {
                "handlers": ["console"],
                "level": "ERROR",
                "propagate": False,
            },
        },
    }


def setup_logging():
    config = get_config()
    logging_names = logging_config()
    logger.remove()

    # Add handlers for Alembic and SQLAlchemy logs
    loggers = {
        name: values["level"] for name, values in logging_names["loggers"].items()
    }

    logger.add(sys.stdout, level=config.LOG_LEVEL, filter=loggers)

    # intercept everything at the root logger
    logging.basicConfig(handlers=[InterceptHandler()], level=config.LOG_LEVEL)
