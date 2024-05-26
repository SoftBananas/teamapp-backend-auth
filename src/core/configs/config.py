import os

from yaml import safe_load
from dotenv import load_dotenv
from loguru import logger
from .db_config import DataBaseConfig
from .hash_config import HashConfig


class Config:
    hash_config: HashConfig
    db_config: DataBaseConfig

    def __init__(
            self,
            config_file: str = "../configs/prod.yml",
            env_file: str = "../.env"
    ) -> None:
        load_dotenv(dotenv_path=env_file)
        with open(config_file, "r") as config_file:
            self.__configs = safe_load(config_file)
        self.__set_configs()

    def __set_configs(self):
        self.hash_config = HashConfig(self.__configs["hash"])
        self.db_config = DataBaseConfig(self.__configs["database"])
        self.__set_logger(self.__configs["logger"])

    @staticmethod
    def __set_logger(config: dict) -> None:
        logger.remove()
        logger.add(
            sink=config["sink"],
            format=config["format"],
            level=config["level"],
            rotation=config["rotation"],
            compression=config["compression"],
        )
