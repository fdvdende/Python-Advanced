import sqlite3
from todo.todo import Status, ToDo

# todo_list = []
#
# def add(todo):
#     todo_list.append(todo)
#
# def get_all():
#     return todo_list

def create_table():
    conn.execute("DROP TABLE IF EXISTS todo")
    conn.execute("""\
CREATE TABLE todo(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  note TEXT,
  deadline TEXT,
  prioriteit TEXT,
  status TEXT,
  active BOOL);""")
    conn.commit()

def add(todo):
    sql = "INSERT INTO todo (note, deadline, prioriteit, status, active) VALUES (?, ?, ?, ?, ?)"
    conn.execute(sql, (todo.note, todo.deadline, todo.prioriteit, str(todo.status), todo.active))
    conn.commit()

def get_all():
    sql = "SELECT * FROM todo"
    cursor = conn.execute(sql)
    for row in cursor.fetchall():
        yield row

def get(id):
    sql = f"SELECT * FROM todo WHERE id = ?"
    cursor = conn.execute(sql, id)
    return cursor.fetchone()

# create connection to database
filename = r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/demos testing/models/todo.db'
conn = sqlite3.connect(filename)

if __name__ == '__main__':
    # create_table()

    id = input('Geef id: ')
    print( get(id) )