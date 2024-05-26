from datetime import datetime

from .annotated_types import uuid_pk, created_at, updated_at
from .base import Base
from sqlalchemy.orm import Mapped


class User(Base):
    __tablename__ = 'user'

    id: Mapped[uuid_pk]
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[datetime | None]
