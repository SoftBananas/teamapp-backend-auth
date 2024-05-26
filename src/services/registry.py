from .abstract import Service
from .hash import HashService
from ..core.configs import Config
from .auth import AuthService
from ..repositories.registry import RepositoryRegistry


class ServiceRegistry:
    def __init__(self, repositories: RepositoryRegistry, config: Config):
        self.hash_service = HashService(config.hash_config)
        self.auth_service = AuthService(repositories.user_repository, self.hash_service)

    def get_services(self) -> list[Service]:
        return [
            self.__dict__[service]
            for service in self.__dict__
            if service.endswith("_service")
        ]