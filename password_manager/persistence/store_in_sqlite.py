import sqlite3

filename = '../data/data.sqlite'


def create_datebase():
    drop_query = 'DROP TABLE IF EXISTS passwords;'
    create_query = 'CREATE TABLE IF NOT EXISTS passwords ( \
                    id INTEGER PRIMARY KEY, \
                    name VARCHAR(80), \
                    url VARCHAR(80), \
                    username VARCHAR(80), \
                    password VARCHAR(80));'

    connection = sqlite3.connect(filename)
    # connection.execute(drop_query)
    connection.execute(create_query)
    connection.commit()


def store(d):
    create_datebase()
    connection = sqlite3.connect(filename)
    sql = 'SELECT name FROM passwords WHERE name=?;'
    result = connection.execute(sql, (d["name"],))
    if result.fetchone():
        sql = 'UPDATE passwords SET url=?, username=?, password=? WHERE name=?;'
        connection.execute(sql, (d["url"], d["username"], d["password"], d["name"]))
        connection.commit()
    else:
        sql = 'INSERT INTO passwords (name, url, username, password) VALUES (?, ?, ?, ?);'
        connection.execute(sql, (d["name"], d["url"], d["username"], d["password"]))
        connection.commit()


def retrieve_one(name):
    connection = sqlite3.connect(filename)
    sql = 'SELECT * FROM passwords WHERE name = ?'
    result = connection.execute(sql, name)
    return result.fetchone()


def retrieve_many(name):
    connection = sqlite3.connect(filename)
    sql = 'SELECT * FROM passwords WHERE name LIKE ?*'
    result = connection.execute(sql, name)
    return list(result.fetchmany())


def get_names():
    connection = sqlite3.connect(filename)
    sql = 'SELECT * FROM passwords'
    result = connection.execute(sql)
    return [item['name'] for item in result.fetchmany()]
