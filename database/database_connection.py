import sqlite3
from sqlite3 import Connection

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._connection = None
        return cls._instance
    
    def connection(self, db_name:str) -> Connection:
        if self._connection is None:
            try:
                self._connection = sqlite3.connect(db_name, check_same_thread=False)
                print("Connection established")
            except sqlite3.Error as error:
                print(error)
        return self._connection
    
    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            print("Connection closed")