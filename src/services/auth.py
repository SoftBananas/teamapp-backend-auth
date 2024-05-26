from src.core.dto.auth import LoginData
from src.core.dto.user import User
from src.repositories.abstract.user import AbstractUserRepository
from src.services.hash import HashService


class AuthService:
    def __init__(self, repository: AbstractUserRepository, hash_service: HashService):
        self.repository = repository
        self.hash = hash_service

    async def authenticate(self, login_data: LoginData) -> bool:
        user: User = await self.repository.get_by_username(login_data.username)
        return self.hash.compare_plain_and_hashed(login_data.password, user.hashed_password)

