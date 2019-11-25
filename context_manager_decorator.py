import sqlite3
from contextlib import contextmanager


@contextmanager
def db_handler(filename):
    conn = sqlite3.connect(filename)
    yield conn
    conn.close()


