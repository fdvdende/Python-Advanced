import secrets
import string
import cryptography
from itertools import cycle
import configparser
import os
import pathlib

rootdirname = pathlib.Path(__file__).parent.parent.parent
filename = pathlib.PurePath(rootdirname, 'config.ini')

config = configparser.ConfigParser()
config.read(filename)
encryption_key = config['encryption']['Key']


class Encryption:
    """This encryption uses XOR

    Methods:
        - encrypt
        - decrypt"""

    encoding = 'utf8'

    @staticmethod
    def encrypt(message: str) -> bytes:
        """Encrypt a message with XOR"""
        encoded = message.encode(Encryption.encoding)
        key = encryption_key.encode()
        encrypted = bytes(c ^ k for c, k in zip(encoded, cycle(key)))
        return encrypted

    @staticmethod
    def decrypt(encrypted: bytes) -> str:
        """Decrypt a message with XOR"""
        key = encryption_key.encode()  # key needs to be a bytes object
        decrypted = bytes(c ^ k for c, k in zip(encrypted, cycle(key)))
        return decrypted.decode(Encryption.encoding)

    @staticmethod
    def generate_random_key(n: int = 32):
        """A stand alone method to generate a random key"""
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(n))

    @staticmethod
    def set_encoding(encoding: str):
        Encryption.encoding = encoding


if __name__ == '__main__':

    print('new key:', Encryption.generate_random_key())

    encrypted = Encryption.encrypt('André')
    print(encrypted)
    print(encrypted.hex())

    decrypted = Encryption.decrypt(encrypted)
    print(decrypted)
