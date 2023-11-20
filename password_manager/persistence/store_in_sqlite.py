import sqlite3

filename = '../data/data.sqlite'


def store(d):
    connection = sqlite3.connect(filename)
    sql = f'INSERT INTO passwords (name, url, username, password) VALUES ({d["name"]}, {d["url"]}, {d["username"]}, {d["password"]})'
    # sql = 'INSERT INTO passwords (name, url, username, password) VALUES (?, ?, ?, ?)'
    connection.executemany(sql, d)
    connection.commit()

def retrieve_one(name):
    pass

def retrieve_many(name):
    pass

def get_names():
    pass