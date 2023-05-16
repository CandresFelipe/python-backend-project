from typing import Callable

from sqlalchemy.orm import Session, registry

mapper_registry = registry()
Sessionmaker = Callable[..., Session]
