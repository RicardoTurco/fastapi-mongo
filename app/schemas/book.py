from bson import ObjectId
from pydantic import BaseModel, field_validator
from typing import Any


class BooksListSchema(BaseModel):
    id: str
    name: str

    @classmethod
    def convert_objectid(cls, v: Any) -> str:
        """Converte ObjectId do MongoDB para string"""
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        from_attributes = True
