import logging
from application import Application
from components import Components
from fastapi.middleware.cors import CORSMiddleware

from asgi_logger.middleware import AccessLoggerMiddleware
from config.models import Config
from config.service import get_config
from database.client import DBClientManager
from router import router


logger_access = logging.getLogger("access")


def create_app(
    config: Config | None = None, db_clientManager: DBClientManager | None = None
) -> Application:
    config = get_config()
    db_clientManager = db_clientManager or DBClientManager.get_from_config(
        config=config.db
    )
    app = Application(on_shutdown=[db_clientManager.shutdown])

    app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(
        AccessLoggerMiddleware,
        format='%(client_addr)s - "%(request_line)s" %(status_code)s',
        logger=logger_access,
    )

    app.components = Components(dbconfig=db_clientManager)

    return app
