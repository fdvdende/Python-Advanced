# relative import for module import and absolute import for running as script
try:
    from .encryption import encrypt, decrypt
except ImportError:
    from encryption import encrypt, decrypt

import json


class Secret:

    def __init__(self, name, *, id = None, content = None, encrypted_content = None):
        self._id = id
        self._name = name
        self._content = None
        if content:
            self.content = content
        if encrypted_content:
            self._encrypted_content = encrypted_content

    def __str__(self):
        return f'Secret: {self._name}'

    def __repr__(self):
        return f'Secret("{self._name}", ...)'

    @property
    def name(self):
        return self._name

    @property
    def encrypted_content(self):
        return self._encrypted_content

    @property
    def content(self):
        if self._encrypted_content:
            return decrypt(self._encrypted_content)

    @content.setter
    def content(self, value):
        self._encrypted_content = encrypt(value)

    # def to_json(self):
    #     return json.dumps(self, indent=4, default=lambda o: {k:str(v) for k, v in o.__dict__.items()})

    def to_dict(self):
        d = {
            'id': self._id,
            'name': self._name,
            'encrypted_content': self._encrypted_content.decode('utf-8')
        }
        return d

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, d):
        id = d['id']
        name = d['name']
        encrypted_content = d['encrypted_content'].encode('utf-8')
        return cls(name, encrypted_content=encrypted_content, id=id)

    @classmethod
    def from_json(cls, s):
        return json.loads(s, object_hook = cls.from_dict)


if __name__ == '__main__':

    secret = Secret('My password', content = 'Welkom2023')

    print(secret)
    print(repr(secret))

    print(secret.encrypted_content)
    print(secret.content)

    s = secret.to_json()
    print(s)

    restored = Secret.from_json(s)
    print('Restored =>', restored)
    print(restored.content)
