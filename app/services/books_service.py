from app.repositories.books import BooksRepository


class BooksService:
    def __init__(self, repository: BooksRepository):
        self.__repository = repository

    async def list_all(self):
        return await self.__repository.list_all(
            {},
            {"_id": 1, "name": 1}
        )
