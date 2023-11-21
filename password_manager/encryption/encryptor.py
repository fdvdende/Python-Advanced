import configparser

from cryptography.fernet import Fernet

filename = 'config.ini'

config = configparser.ConfigParser()
config.read(filename)
key = bytes(config['encryption']['key'], 'utf8')

# key = b'O7t1sce1zWza1YY-RtJMPygbnjFgBc47g2SVtGmynzw='

def encrypt(original):
    pass

def decrypt(encrypted):
    pass


if __name__ == '__main__':

    # key = Fernet.generate_key()
    # print(key)
    #
    f = Fernet(key)

    original = b"A really secret message. Not for prying eyes."
    print(original)

    encrypted = f.encrypt(original)
    print(encrypted)

    decrypted = f.decrypt(encrypted)
    print(decrypted)





