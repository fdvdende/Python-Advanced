from cryptography.fernet import Fernet

import hashlib
import configparser

config = configparser.ConfigParser()
config.read('/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project C/config.ini')  # todo - kan dit beter??
key = config['encryption']['Key']


def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


def encrypt(text):
    f = Fernet(key)
    return f.encrypt(text.encode())


def decrypt(encrypted):
    f = Fernet(key)
    return f.decrypt(encrypted).decode()


# ----------------------------------------------------------------------------------


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('../../config.ini')         # todo kan dit beter??
    print(config.sections())
    print(config['encryption']['Key'])

    s = 'abcdefgh'

    print(get_hash(s))

    encrypted = encrypt(s)
    print(encrypted)

    decrypted = decrypt(encrypted)
    print(decrypted)

    print(decrypted == s)
