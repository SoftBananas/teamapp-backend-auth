from .postgres.user import PostgresUserRepository
from ..core.database import DataBase


class RepositoryRegistry:
    def __init__(self, db: DataBase):
        self.user_repository = PostgresUserRepository(db)
