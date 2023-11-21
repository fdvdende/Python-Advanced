import logging
import time

logging.basicConfig(
    filename = None,
    level = logging.DEBUG
)

from password_manager.encryption.encryptor import Encryptor


def timer(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        return_value = func(*args, **kwargs)
        t1 = time.time()
        print(f'Duration {t1 - t0}s')
        return return_value
    return wrapper


last_t = time.time() - 1
def throttle(func):
    def wrapper(*args, **kwargs):
        global last_t
        t0 = time.time()
        if (t0 - last_t) > 1:
            return_value = func(*args, **kwargs)
        else:
            print('Too many attempts!!!')
            return_value = False
        last_t = t0
        return return_value
    return wrapper



def logger(func):
    def wrapper(*args, **kwargs):
        logging.debug(f'In functie {func.__name__}.')
        return_value = func(*args, **kwargs)
        return return_value
    return wrapper



class PasswordBroker:

    def __init__(self, name, url, username, password):
        self._name = name
        self._url = url
        self._username = username
        encryptor = Encryptor()
        self._password = encryptor.encrypt(password)
        self._hash = hash(password)

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        encryptor = Encryptor()
        return encryptor.decrypt(self._password)

    @throttle
    def validate_password(self, test_password):
        test_hash = hash(test_password)
        return test_hash == self._hash

    def __str__(self):
        return f'{self._name} {self._url} {self._username}'

    def __repr__(self):
        arg_string = ', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())
        return f'PasswordBroker({arg_string})'

    def to_json(self):
        return {
            'name': self._name,
            'url': self._url,
            'username': self._username,
            'password': self._password
        }



if __name__ == '__main__':

    broker = PasswordBroker('Peter', 'nu.nl', 'pa', 'jhsdfgkasjhf')

    print(broker)
    print(repr(broker))
    print(broker.to_json())
    print(broker.password)

    print(broker.validate_password('abcd'))
    print(broker.validate_password('dsf'))
    print(broker.validate_password('abcdfgdfhdd'))
    print(broker.validate_password('jhsdfgkasjhf'))
    time.sleep(2)
    print(broker.validate_password('jhsdfgkasjhf'))

