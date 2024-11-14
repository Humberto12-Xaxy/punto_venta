import sqlite3

from database.database_connection import DatabaseConnection


def check_sqlite() -> bool:
    try:
        with DatabaseConnection().connection("db.sqlite3") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name from sqlite_master WHERE type='table';")
            cursor.fetchall()
            for table in cursor.fetchall():
                print(table[0])
            if cursor.rowcount == 0:
                return False
            cursor.close()
            return True
    except sqlite3.OperationalError:
        return False