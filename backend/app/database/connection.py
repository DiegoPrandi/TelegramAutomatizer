import sqlite3;

databaseName = 'telegram_automatizer.db'

def get_connection():
    conn = sqlite3.connect(databaseName)
    conn.row_factory = sqlite3.Row
    return conn