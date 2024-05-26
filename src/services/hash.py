from passlib.context import CryptContext

from .abstract import Service
from ..core.configs.hash_config import HashConfig


class HashService(Service):
    def __init__(self, config: HashConfig):
        self.context = CryptContext(schemes=config.schemas, deprecated=config.deprecated)

    def get_hash(self, string: str) -> str:
        return self.context.hash(string)

    def compare_plain_and_hashed(self, plain: str, hashed: str) -> bool:
        return self.context.verify(plain, hashed)
