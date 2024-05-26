import uuid

from loguru import logger
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from ...core.database import DataBase
from ...core.models.sqlalchemy import Base
from ..abstract.abstract import AbstractRepository


class PostgresRepository(AbstractRepository):
    model_table: type[Base] = Base

    def __init__(self, database: DataBase):
        self.db = database

    async def create(self, model: model_table) -> uuid.UUID | int:
        try:
            async with self.db.session_maker() as session:
                model_id = await session.execute(
                    insert(self.model_table)
                    .values(**self.get_filled_fields(model))
                    .returning(self.model_table.id)
                )
                await session.commit()
            return model_id.one()[0]
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def get(self, model_id: uuid.UUID | int) -> model_table | None:
        try:
            async with self.db.session_maker() as session:
                models = await session.execute(
                    select(self.model_table).filter(self.model_table.id == model_id)
                )
            row = models.first()
            if row is not None:
                return row[0]
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            raise error

    async def get_all(self) -> list[model_table]:
        try:
            async with self.db.session_maker() as session:
                models = await session.execute(select(self.model_table))
            rows = models.all()
            return [row[0] for row in rows]
        except Exception as error:
            logger.error(str(error))
            raise error

    async def update(self, model: model_table) -> None:
        try:
            async with self.db.session_maker() as session:
                await session.execute(
                    update(self.model_table)
                    .values(**self.get_filled_fields(model))
                    .filter(self.model_table.id == model.id)
                    .returning(self.model_table.id)
                )
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def delete(self, model_id: uuid.UUID | int) -> None:
        try:
            async with self.db.session_maker() as session:
                await session.execute(
                    delete(self.model_table).where(self.model_table.id == model_id)
                )
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def delete_all(self) -> None:
        try:
            async with self.db.session_maker() as session:
                await session.execute(delete(self.model_table))
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    @staticmethod
    def get_filled_fields(model: model_table) -> dict:
        return {
            column: value
            for column, value in model.get_dict().items()
            if value is not None
        }