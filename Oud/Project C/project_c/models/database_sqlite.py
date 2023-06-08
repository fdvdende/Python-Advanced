import sqlite3

class Database:

    filename = '/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project C/data/database.sqlite'

    def __init__(self):
        self._connection = sqlite3.connect(self.filename)
        self._cursor = self._connection.cursor()
        self.build_users_table()
        self.build_secrets_table()

    def __del__(self):
        self._connection.close()

    def build_users_table(self):
        sql = 'CREATE TABLE IF NOT EXISTS users ( \
               id INTEGER PRIMARY KEY, \
               name VARCHAR(80), \
               hash VARCHAR(1024));'
        self._connection.execute(sql)
        self._connection.commit()

    def build_secrets_table(self):
        sql = 'CREATE TABLE IF NOT EXISTS secrets ( \
               id INTEGER PRIMARY KEY, \
               user_id INTEGER, \
               name VARCHAR(80), \
               secret VARCHAR(1024));'
        self._connection.execute(sql)
        self._connection.commit()

    # CRUD - Create Read Update Delete

    def insert_user(self, username, password_hash):
        insert_query = 'INSERT INTO users (name, hash) VALUES (?, ?)'
        self._connection.execute(insert_query, (username.lower(), password_hash))
        self._connection.commit()

    def update_or_insert_user(self, username, password_hash):
        user_id =  self.get_user_id(username)
        if user_id:
            update_query = 'UPDATE users SET hash = ? WHERE id = ?'
            self._connection.execute(update_query, (password_hash, user_id))
            self._connection.commit()
        else:
            self.insert_user(username, password_hash)

    def get_user(self, username):
        select_query = 'SELECT * FROM users WHERE name = ?'
        result = self._cursor.execute(select_query, (username.lower(), ))
        self._connection.commit()
        return result.fetchone()

    def get_all_users(self):
        select_query = 'SELECT * FROM users'
        result = self._cursor.execute(select_query)
        self._connection.commit()
        return result.fetchall()

    def remove_user(self, username):
        delete_query = 'DELETE FROM users WHERE name = ?'
        self._connection.execute(delete_query, (username.lower(), ))
        self._connection.commit()

    def get_user_id(self, username):
        select_query = 'SELECT id FROM users WHERE name = ?'
        result = self._cursor.execute(select_query, (username.lower(), ))
        self._connection.commit()
        try:
            return result.fetchone()[0]
        except:
            return

    def insert_secret(self, username, name, secret):
        user_id = self.get_user_id(username.lower())
        insert_query = 'INSERT INTO secrets (user_id, name, secret) VALUES (?, ?, ?)'
        self._connection.execute(insert_query, (user_id, name.lower(), secret))
        self._connection.commit()

    def update_or_insert_secret(self, username, name, secret):
        existing_record = self.get_secret(username, name)
        if existing_record:
            id, *_ = existing_record
            update_query = 'UPDATE secrets SET name = ?, content = ? WHERE id = ?'
            self._connection.execute(update_query, (name.lower(), secret, id))
            self._connection.commit()
        else:
            self.insert_secret(username, name, secret)

    def get_secret(self, username, name):
        user_id = self.get_user_id(username.lower())
        select_query = 'SELECT * FROM secrets WHERE user_id = ? AND name = ?'
        result = self._cursor.execute(select_query, (user_id, name.lower()))
        self._connection.commit()
        return result.fetchone()

    def get_all_secrets(self, username):
        user_id = self.get_user_id(username.lower())
        select_query = 'SELECT * FROM secrets WHERE user_id = ?'
        result = self._cursor.execute(select_query, (user_id, ))
        self._connection.commit()
        return result.fetchall()

    def remove_secret(self, username, name):
        user_id = self.get_user_id(username.lower())
        delete_query = 'DELETE FROM secrets WHERE user_id = ? AND name = ?'
        self._connection.execute(delete_query, (user_id, name.lower()))
        self._connection.commit()

    def remove_all_secrets(self, username):
        user_id = self.get_user_id(username.lower())
        delete_query = 'DELETE FROM secrets WHERE user_id = ?'
        self._connection.execute(delete_query, (user_id, ))
        self._connection.commit()


# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    db = Database()

    db.build_users_table()
    db.build_secrets_table()

    db.remove_all_secrets('peter')
    db.remove_user('peter')
    db.remove_all_secrets('aljoscha')
    db.remove_user('aljoscha')

    db.insert_user('peter', 'abcd')
    db.insert_user('aljoscha', 'abcd')

    db.insert_secret('peter', 'password', 'abcdefg')
    db.insert_secret('peter', 'pin', '1234')

    db.insert_secret('aljoscha', 'wachtwoord', 'abcdefg')
    db.insert_secret('aljoscha', 'pincode', '6789')

    for user_id, username, hash in db.get_all_users():
        print(f'Gebruiker: {username}')
        print('Geheimen')
        for _, _, name, secret in db.get_all_secrets(username):
            print(f'{name}: {secret}')
