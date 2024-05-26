from abc import ABC, abstractmethod

from src.core.dto.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        raise NotImplementedError
