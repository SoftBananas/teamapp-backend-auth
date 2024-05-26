import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: uuid.UUID
    email: str
    username: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
