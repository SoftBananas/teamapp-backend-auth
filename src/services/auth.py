from ..core.dto.auth import LoginData
from ..core.dto.user import User
from ..repositories.abstract.user import AbstractUserRepository
from .abstract import Service
from .hash import HashService


class AuthService(Service):
    def __init__(self, repository: AbstractUserRepository, hash_service: HashService):
        self.repository = repository
        self.hash = hash_service

    async def authenticate(self, login_data: LoginData) -> bool:
        user: User = await self.repository.get_by_username(login_data.username)
        if user:
            return self.hash.compare_plain_and_hashed(login_data.password, user.hashed_password)


