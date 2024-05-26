import os


class DataBaseConfig:
    def __init__(
        self, config: dict
    ):
        self.driver = config["driver"]
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")
