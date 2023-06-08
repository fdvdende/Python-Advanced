import os.path
import sqlite3
from textwrap import dedent
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
filename = config['sqlite']['database']
print(filename)

def create_table():
    with sqlite3.connect(filename) as conn:
        conn.execute("DROP TABLE IF EXISTS todo")
        sql = dedent("""\
            CREATE TABLE todo(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                note TEXT,
                deadline TEXT,
                prioriteit TEXT,
                status TEXT,
                active BOOL)""")
        conn.execute(sql)
        conn.commit()

def add(todo):
    with sqlite3.connect(filename) as conn:
        sql = "INSERT INTO todo (note, deadline, prioriteit, status, active) VALUES (?, ?, ?, ?, ?)"
        conn.execute(sql, (todo.note, todo.deadline, todo.prioriteit, str(todo.status), todo.active))
        conn.commit()

def get_all():
    with sqlite3.connect(filename) as conn:
        sql = "SELECT * FROM todo"
        cursor = conn.execute(sql)
        for row in cursor.fetchall():
            yield row

def get(id):
    with sqlite3.connect(filename) as conn:
        sql = "SELECT * FROM todo WHERE id = ?"
        cursor = conn.execute(sql, id)
        return cursor.fetchone()


if __name__ == '__main__':
    create_table()
