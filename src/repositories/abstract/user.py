from abc import ABC, abstractmethod

from src.core.dto.user import User
from src.repositories.abstract.abstract import AbstractRepository


class AbstractUserRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        raise NotImplementedError
