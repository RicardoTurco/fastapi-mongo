from uuid import UUID
from pydantic import BaseModel


class BookResponseSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        json_encoders = {UUID: str}
        from_attributes = True
