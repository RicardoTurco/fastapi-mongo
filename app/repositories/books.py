from typing import Dict, List

from config import settings


class BooksRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = settings.BOOK_COLLECTION
        self.__db_connection = db_connection

    async def list_all(self, filters: Dict, return_options: Dict) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        books = collection.find(
            filters,
            return_options
        ).to_list()
        books = [{**book, "id": str(book.pop("_id"))} for book in books]
        return books
