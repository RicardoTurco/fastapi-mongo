from pymongo import MongoClient
from config import settings


class DBConnectionHandler:
    """
    class DBConnectionHandler
    """
    def __init__(self) -> None:
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            settings.USERNAME,
            settings.PASSWORD,
            settings.HOST,
            settings.PORT
        )
        self.__database_name = settings.DB_NAME
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        """
        Make a connection to Database.
        """
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        """
        Returns a db connection.

        :return: db_connection;
        """
        return self.__db_connection

    def get_db_client(self):
        """
        Returns a db client;

        :return: db_client;
        """
        return self.__client

def make_conn():
    db_handle = DBConnectionHandler()
    db_handle.connect_to_db()
    db_conn = db_handle.get_db_connection()
    return db_conn
