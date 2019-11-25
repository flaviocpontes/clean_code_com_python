import sqlite3


class DBHandler:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.conn = sqlite3.connect(self.filename)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

