
class PasswordBroker:

    def __init__(self, name, url, username, password):
        self.name = name
        self.url = url
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.name} {self.url} {self.username}'

    def __repr__(self):
        arg_string = ', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())
        return f'PasswordBroker({arg_string})'

    def to_json(self):
        return {
            'name': self.name,
            'url': self.url,
            'username': self.username,
            'password': self.password
        }



if __name__ == '__main__':

    broker = PasswordBroker('Peter', 'nu.nl', 'pa', 'jhsdfgkasjhf')

    print(broker)
    print(repr(broker))