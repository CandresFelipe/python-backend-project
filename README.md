# python-backend-project

Project where I build a small backend API for doing e-commerce requests. This app is built using [FastAPI](https://fastapi.tiangolo.com/) framework.

For database connection tool I use [SQlAlchemy](https://docs.sqlalchemy.org/en/20/index.html) library that facilitates the conversation with python and database.

## Prerequisites

1. Install [Python 3.10](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)
2. Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
3. Install [Postgresql](https://www.postgresql.org/download/)


## Steps to install this project locally.

1. After you have been install globally in your machine the previous programs, in your bash terminal (or zsh) run the virtual environment
   where the project will be running. if you don't know what a virtual environment is, check [here](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20created,the%20virtual%20environment%20are%20available.) 

   This can be activated by running:
   `poetry shell`

   poetry is a package dependencies and virtual environments manager so when you run the shell we internally run:
   `source .venv/bin/activate`

2. To run the API for now is just:
   `python src/app/main.py`