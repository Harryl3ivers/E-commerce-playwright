import sqlite3

connection = sqlite3.connect("database/test_database.db")

with open("database/setup.sql") as file:
    connection.executescript(file.read())

connection.commit()
connection.close()