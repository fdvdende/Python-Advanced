import pickle
import pathlib
import sqlite3


try:
    from .secret import Secret
except ImportError:
    from secret import Secret

try:
    from .encryption import Encryption
except ImportError:
    from encryption import Encryption


rootdirname = pathlib.Path(__file__).parent.parent.parent


class PersistenceWithPickle:

    filename = pathlib.PurePath(rootdirname, 'data', 'secrets.pickle')

    @staticmethod
    def store(data):
        with open(PersistenceWithPickle.filename, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def retrieve():
        with open(PersistenceWithPickle.filename, 'rb') as f:
            return pickle.load(f)


class PersistenceWithSQLite:

    filename = pathlib.PurePath(rootdirname, 'data', 'secrets.db')

    @staticmethod
    def create_table():
        sql = """\
            CREATE TABLE secrets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                content TEXT,
                owner TEXT
            );"""
        conn = sqlite3.connect(PersistenceWithSQLite.filename)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def get_secrets():
        sql = "SELECT name, content, owner FROM secrets;"
        conn = sqlite3.connect(PersistenceWithSQLite.filename)
        cursor = conn.cursor()
        cursor.execute(sql)
        secrets = []
        for record in cursor.fetchall():
            content = Encryption.decrypt(record[1])
            secrets.append(Secret(record[0], content, record[2]))
        conn.commit()
        conn.close()
        return secrets

    @staticmethod
    def store_secret(secret):
        sql = "INSERT INTO secrets (name, content, owner) VALUES (?, ?, ?);"
        conn = sqlite3.connect(PersistenceWithSQLite.filename)
        cursor = conn.cursor()
        cursor.execute(sql, (secret.name, secret.encrypted_content, secret.owner))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_secret(name, owner):
        sql = "DELETE FROM secrets WHERE name = ? AND owner = ?;"
        conn = sqlite3.connect(PersistenceWithSQLite.filename)
        cursor = conn.cursor()
        cursor.execute(sql, (name, owner))
        conn.commit()
        conn.close()

# -------------------------------------

if __name__ == '__main__':

    PersistenceWithSQLite.create_table()
