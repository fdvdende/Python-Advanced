import configparser

from cryptography.fernet import Fernet


class Encryptor:

    config_filename = '../encryption/config.ini'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Encryptor.config_filename)
        key = bytes(config['encryption']['key'], 'utf8')
        self._cypher = Fernet(key)

    def encrypt(self, original: str) -> bytes:
        return self._cypher.encrypt(bytes(original, 'utf8'))

    def decrypt(self, encrypted: bytes) -> str:
        return str(self._cypher.decrypt(encrypted), 'utf8')


if __name__ == '__main__':

    # key = Fernet.generate_key()
    # print(key)
    #
    # key = b'O7t1sce1zWza1YY-RtJMPygbnjFgBc47g2SVtGmynzw='

    encryptor = Encryptor()

    original = 'A really secret message. Not for prying eyes.'
    print(original)

    encrypted = encryptor.encrypt(original)
    print(encrypted)

    decrypted = encryptor.decrypt(encrypted)
    print(decrypted)







