# from src.models.encryption import Encryption

try:
    from .encryption import Encryption
except ImportError:
    from encryption import Encryption





class Secret:

    def __init__(self, name: str, content: str, owner: str):
        self._name = name
        self._content = Encryption.encrypt(content)
        self._owner = owner

    def __repr__(self) -> str:
        return f'Secret("{self._name}", "...", "{self._owner}")'

    def __str__(self) -> str:
        return f'Secret - {self._name} - {self._owner}'

    @property
    def name(self) -> str:
        return self._name

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def content(self) -> str:
        return Encryption.decrypt(self._content)

    @property
    def encrypted_content(self) -> bytes:
        return self._content


# ------------------------------------------

if __name__ == '__main__':

    secret = Secret('wachtwoord', 'Welkom2023!', 'peter')

    print(repr(secret))
    print(str(secret))

    print(secret.content)
