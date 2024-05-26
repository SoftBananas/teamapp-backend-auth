from typing import Any


class HashConfig:
    def __init__(self, configs: dict[str, Any]):
        self.schemas: list[str] = configs["schemas"]
        self.deprecated: str = configs["deprecated"]
