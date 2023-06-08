from project_c.models.user import User
from project_c.models.secret import Secret

import pickle


def main():

    user_name = input('Geef naam: ')
    user_password = input('Geef wachtwoord: ')

    user = User(user_name)
    user.set_password(user_password)

    print('Voer nu jouw geheimen in.')
    while True:

        secret_name = input('Naam: ')

        if secret_name == '':
            break

        secret_content = input('Geheim: ')

        user.add_secret(secret_name, secret_content)

    filename = 'data/user.pickle'
    with open(filename, 'wb') as f:
        pickle.dump(user, f)


if __name__ == '__main__':
    main()
