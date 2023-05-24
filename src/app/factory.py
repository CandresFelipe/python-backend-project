from application import Application
from components import Components
from fastapi.middleware.cors import CORSMiddleware

from config.models import Config
from config.service import get_config
from database.client import DBClientManager
from router import router


def create_app(
    config: Config | None = None, db_clientManager: DBClientManager | None = None
) -> Application:
    config = get_config()
    db_clientManager = db_clientManager or DBClientManager.get_from_config(
        config=config.db
    )

    app = Application(debug=config.DEBUG, on_shutdown=[db_clientManager.shutdown])
    db_clientManager.create_or_update_models()
    app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.components = Components(dbconfig=db_clientManager)

    return app
