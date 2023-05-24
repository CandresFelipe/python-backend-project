import subprocess

import click
from sqlalchemy.exc import OperationalError

from database.client import DBClientManager

cmd = "sudo service postgresql start"


def check_database_connection(db_clientManager: DBClientManager):
    try:
        with db_clientManager.engine.connect():
            click.echo("Database connection established")
            return True
    except OperationalError as exc:
        click.echo(f"Failed to connect to database info err: {exc}")
        return False


def check_postgresql_service():
    try:
        subprocess.run(cmd, shell=True, check=True)
        click.echo("PostgreSQL service started")
    except subprocess.CalledProcessError:
        click.echo("Failed to start postgreSQL service")
