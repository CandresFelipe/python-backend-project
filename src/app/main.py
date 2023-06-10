from app_logging import setup_logging
import click
from services import check_database_connection, check_postgresql_service
from sqlalchemy_utils import create_database, database_exists
from config.service import get_config
from database.client import DBClientManager


@click.command()
def check_postgres_server() -> None:
    config = get_config()
    db_manager = DBClientManager.get_from_config(config.db)
    if not check_database_connection(db_manager):
        check_postgresql_service()


@click.command()
def init_database() -> None:
    config = get_config()

    if database_exists(config.db.URI):
        print("Database already exist")
    else:
        create_database(config.db.URI)

    # run migrations
    database_client = DBClientManager(config.db.URI)
    database_client.run_migrations()


@click.command()
@click.option("--host", default="localhost", help="Server host")
@click.option("--port", default=5000, help="Server host")
def init_app(host, port):
    import uvicorn
    from app_logging import logging_config

    config = uvicorn.Config(
        "app.factory:create_app",
        host=host,
        port=port,
        factory=True,
        log_config=logging_config(),
    )
    server = uvicorn.Server(config)
    setup_logging()
    server.run()


@click.group()
def cli() -> None:
    ...


@click.command()
def start() -> None:
    import subprocess

    subprocess.run(["python", "src/app/main.py", "check-postgres-server"])
    subprocess.run(["python", "src/app/main.py", "init-database"])
    subprocess.run(["python", "src/app/main.py", "init-app"])


cli.add_command(check_postgres_server)
cli.add_command(init_database)
cli.add_command(init_app)
cli.add_command(start)

if __name__ == "__main__":
    cli()
