from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    class BookModel
    """
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str = Field(..., min_length=5, max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)

    class Config:
        """
        Configurations of BookModel class
        """
        populate_by_name = True
        json_encoders = {UUID: str}
