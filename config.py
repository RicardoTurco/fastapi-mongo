import logging

from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Application general settings class, which inherits from 'BaseSettings' from pydantic.
    """

    APP_NAME: str = "fastapi-mongo"

    HOST: str = "localhost"
    PORT: str = "27017"
    USERNAME: str = "admin"
    PASSWORD: str = "pass"
    DB_NAME: str = "fastapi-mongo"
    BOOK_COLLECTION: str = "my-books"

    class Config:
        """
        Configurations of pydantic ...
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
