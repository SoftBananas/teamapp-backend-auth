from .postgres import PostgresRepository
from ..abstract.user import AbstractUserRepository
from ...core.dto.user import User


class PostgresUserRepository(AbstractUserRepository, PostgresRepository):
    model_table = User

    async def get_by_username(self, username: str) -> User:
        pass