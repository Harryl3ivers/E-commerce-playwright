import sqlite3

DATABASE = "database/test_database.db"

def get_connection():
    return sqlite3.connect(DATABASE)