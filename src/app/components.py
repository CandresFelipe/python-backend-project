from dataclasses import dataclass

from config.models import DBConfig

"""this decorator automatically adds special method such
as __init__() and __repr__() to uer-defined classes"""


@dataclass
class Components:
    dbconfig: DBConfig
