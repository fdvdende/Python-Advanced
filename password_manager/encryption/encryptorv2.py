import configparser
from cryptography.fernet import Fernet

class ConfigEncryptor:
    def __init__(self, config_file='config.ini', section='encryption', key_name='key'):
        self.config_file = config_file
        self.section = section
        self.key_name = key_name
        self.key = self.load_key()

        if self.key is None:
            self.key = Fernet.generate_key()
            self.save_key()

        self.cipher = Fernet(self.key)

    def load_key(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        try:
            key = bytes(config[self.section][self.key_name], 'utf8')
            return key
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

    def save_key(self):
        config = configparser.ConfigParser()
        config[self.section] = {self.key_name: self.key.decode('utf8')}
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)

    def encrypt(self, original):
        encrypted = self.cipher.encrypt(original)
        return encrypted

    def decrypt(self, encrypted):
        decrypted = self.cipher.decrypt(encrypted)
        return decrypted

if __name__ == '__main__':
    encryptor = ConfigEncryptor()

    original = b"A really secret message. Not for prying eyes."
    print("Original:", original)

    encrypted = encryptor.encrypt(original)
    print("Encrypted:", encrypted)

    decrypted = encryptor.decrypt(encrypted)
    print("Decrypted:", decrypted)
