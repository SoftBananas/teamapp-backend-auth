from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from ..configs.config import DataBaseConfig
from .connection import Connection
from .session_maker import SessionMaker


class DataBase:
    def __init__(self, db_config: DataBaseConfig):
        self.config = db_config
        self.connection = Connection(self.config)
        self.session_maker = SessionMaker(self.connection)

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session
