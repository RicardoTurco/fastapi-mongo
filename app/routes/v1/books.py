import logging
from fastapi import APIRouter, Depends, Response, status
from typing import List

from app.database.connection import make_conn
from app.repositories.books import BooksRepository
from app.services.books_service import BooksService
from app.schemas.book import BookResponseSchema

logger = logging.getLogger(__name__)

books_router = APIRouter()

TAG = "Books"


def get_book_service(db=Depends(make_conn)):
    repository = BooksRepository(db)
    return BooksService(repository)


@books_router.get(
    "/books",
    tags=[TAG],
    summary="Retrieves all books.",
    description="This endpoint retrieves all books.",
    status_code=status.HTTP_200_OK,
    response_model=List[BookResponseSchema]
)
async def all_books(service: BooksService = Depends(get_book_service)):
    books = await service.list_all()
    return books
