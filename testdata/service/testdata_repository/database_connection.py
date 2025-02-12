import sqlite3

class DatabaseConnection:
    """
        Implementation of the database connection,

        Author:
            Mirko Werner
        """
    def __init__(self, db_file: str):
        self.db_file = db_file

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()