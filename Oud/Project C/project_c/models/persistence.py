try:
    from .user import User
    from .secret import Secret
    from . import database_sqlite
    from . import exceptions
except ImportError:
    from user import User
    from secret import Secret
    import database_sqlite
    import exceptions

import pickle


class PersistencePickle:

    filename = '/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project C/data/users.pickle'

    def __init__(self):
        try:
            with open(self.filename, 'rb') as f:
                self._users = pickle.load(f)
        except FileNotFoundError:
            self._users = []

    def get_user_names(self):
        return [user.name for user in self._users]

    def save_user(self, user):
        self.remove_user(user.name)
        self._users.append(user)

    def remove_user(self, user_name):
        for i, user in enumerate(self._users):
            if user.name.lower() == user_name.lower():
                del self._users[i]
                break

    def get_user(self, user_name):
        for i, user in enumerate(self._users):
            if user.name.lower() == user_name.lower():
                return user

    def close(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self._users, f)


class PersistenceSqlite:

    def __init__(self):
        self._database = database_sqlite.Database()

    def get_user_names(self):
        return [name for id, name, hash in self._database.get_all_users()]

    def save_user(self, user):
        self._database.update_or_insert_user(user.name, user.password_hash)
        self._database.remove_all_secrets(user.name)
        for secret_name in user.secret_names:
            secret = user.get_secret(secret_name)
            self._database.insert_secret(user.name, secret_name, secret.encrypted_content)

    def remove_user(self, user_name):
        self._database.remove_all_secrets(user_name)
        self._database.remove_user(user_name)

    def get_user(self, user_name):
        record = self._database.get_user(user_name)
        if record:
            id, name, password_hash = record
            user = User(name, id = id, password_hash = password_hash)

            records = self._database.get_all_secrets(user_name)
            for record in records:
                id, user_id, name, encrypted_content = record
                secret = Secret(name, encrypted_content = encrypted_content, id = id)
                user._secrets.append(secret)

            return user

    def close(self):
        pass

class PersistenceMongoDB:

    def get_user_names(self):
        pass

    def save_user(self, user):
        pass

    def remove_user(self, username):
        pass

    def get_user(self, username):
        pass

    def close(self):
        pass


class Persistence(PersistenceSqlite):
    pass
