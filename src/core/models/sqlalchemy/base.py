from typing import Any

from sqlalchemy import JSON, MetaData, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped

from .annotated_types import int_pk, uuid_pk


class Base(DeclarativeBase):
    metadata = MetaData()
    type_annotation_map = {dict[str, Any]: JSON}

    def get_dict(self) -> dict:
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }
