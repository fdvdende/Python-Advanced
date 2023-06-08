import string
import json

try:
    from .secret import Secret
    from .encryption import get_hash
    from . import exceptions
except ImportError:
    from secret import Secret
    from encryption import get_hash
    import exceptions


class User:
    """A user model for our secret application"""

    def __init__(self, name: str, *, id = None, password_hash = None):
        self._id = id
        self._name = name
        self._password_hash = password_hash
        self._secrets = []

    def __str__(self):
        return f'User: {self._name}'

    def __repr__(self):
        return f'User("{self._name}")'

    @property
    def name(self):
        return self._name

    @property
    def password_hash(self):
        return self._password_hash

    @property
    def secrets(self):
        return self._secrets

    @property
    def secret_names(self):
        return [secret.name for secret in self._secrets]

    @staticmethod
    def is_valid_password(password,
                          min_length = 8,
                          min_lowercase = 1,
                          min_uppercase = 1,
                          min_digits = 1,
                          min_special = 1):

        if len(password) < min_length:
            return False
        elif len(set(password) & set(string.ascii_lowercase)) < min_lowercase:
            return False
        elif len(set(password) & set(string.ascii_uppercase)) < min_uppercase:
            return False
        elif len(set(password) & set(string.digits)) < min_digits:
            return False
        elif len(set(password) & set(string.punctuation)) < min_special:
            return False
        else:
            return True

    def set_password(self, password):
        if self.is_valid_password(password):
            self._password_hash = get_hash(password)
        else:
            raise exceptions.InvalidPasswordException('Invalid password')

    def check_password(self, password):
        return self._password_hash == get_hash(password)

    def add_secret(self, secret):
        self._secrets.append(secret)

    def get_secret(self, name):
        for secret in self._secrets:
            if secret.name.lower() == name.lower():
                return secret
        else:
            raise exceptions.SecretNotFoundException(f'Secret with name {name} does not exists.')

    def remove_secret(self, name):
        for i, secret in enumerate(self._secrets):
            if secret.name.lower() == name.lower():
                del self._secrets[i]

    def to_json(self):
        d = {
            'id': self._id,
            'name': self._name,
            'password_hash': self._password_hash,
            'secrets': [secret.to_json() for secret in self._secrets]
        }
        return json.dumps(d)

    @classmethod
    def from_dict(cls, d):
        id = d['id']
        name = d['name']
        password_hash = d['password_hash']
        p = User(name, id = id, password_hash = password_hash)
        p._secrets = [Secret.from_json(secret_json) for secret_json in d['secrets']]
        return p

    @classmethod
    def from_json(cls, s):
        return json.loads(s, object_hook = cls.from_dict)


# -------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    user = User('Peter')
    print(user)

    password = 'abcABC333###'
    user.set_password(password)
    print(user.check_password(password))

    print(user.name)

    user.add_secret(Secret('password', 'Welkom132'))
    user.add_secret(Secret('wachtwoord', 'ABCD'))

    retrieved = user.get_secret('password')

    print(retrieved.content)

    password = 'abc'
    print(password, User.is_valid_password(password))

    password = 'abcABC1&'
    print(password, User.is_valid_password(password))

    print(user.to_json())