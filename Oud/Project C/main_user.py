from project_c.models.user import User
from project_c.models.secret import Secret
from project_c.models import exceptions
from project_c.models.logging_setup import logging
from project_c.models.persistence import Persistence

import sys


def menu():
    options = {
        1: 'Overzicht',
        2: 'Geheim inzien',
        3: 'Geheim toevoegen',
        4: 'Geheim verwijderen',
        5: 'Wachtwoord wijzigen',
        6: 'Stoppen',
    }

    menu = '\nMogelijke acties:\n' + '\n'.join(f'{k}) {v}' for k, v in options.items())

    while True:
        try:
            print(menu)
            choice = int(input('Wat wil je doen? '))
            if 1 <= choice <= len(menu):   # choice >= 1 and choice <= 5
                print()
                return choice
            else:
                assert False, 'Illegal.'
        except:
            print('Probeer nogmaals.')


def login():
    global persistence

    print('Login')
    user_name = input('Geef naam: ')
    user_password = input('Geef wachtwoord: ')

    user = persistence.get_user(user_name)

    if user:
            if user.check_password(user_password):
                logging.info(f'User {user.name} logged in.')
                return user
            else:
                logging.info(f'User {user.name} tried to log in with password {user_password}.')
                print('Wachtwoord is niet correct')
                raise exceptions.UnsuccesfulLoginException('Incorrect password')
    else:
        logging.info(f'Unknown user tried to log in with name {user_name}.')
        print('Naam is niet bekend')
        raise exceptions.UnsuccesfulLoginException('Unknown user')


def main():
    global persistence
    persistence = Persistence()

    try:
        user = login()
    except exceptions.UnsuccesfulLoginException:
        sys.exit()

    while True:
        choice = menu()

        match choice:

            case 1:
                if len(user.secrets) == 0:
                    print('Er zijn geen geheimen.')
                else:
                    print('Geheimen:')
                    for secret in user.secrets:
                        print(secret)

            case 2:
                secret_name = input('Geef naam van het geheim dat je wilt inzien: ')

                try:
                    secret = user.get_secret(secret_name)
                    print(secret.name)
                    print(secret.content)
                except exceptions.SecretNotFoundException:
                    print('Een geheim met die naam bestaat niet.')

            case 3:
                secret_name = input('Geef naam van het geheim dat je wilt toevoegen: ')
                secret_content = input('Wat is het geheim dat je wilt toevoegen: ')

                user.add_secret(Secret(secret_name, content = secret_content))
                print('Het geheim is toegevoegd.')

            case 4:
                secret_name = input('Geef naam van het geheim dat je wilt verwijderen: ')

                try:
                    user.remove_secret(secret_name)
                    print('Het geheim is verwijderd.')
                except exceptions.SecretNotFoundException:
                    print('Een geheim met die naam bestaat niet.')

            case 5:
                user_password = input('Geef nieuwe wachtwoord: ')

                try:
                    user.set_password(user_password)
                    print('Wachtwoord is gewijzigd.')
                except exceptions.InvalidPasswordException:
                    print('Dat wachtwoord voldoet niet aan de eisen.')

            case 6:
                logging.info(f'User {user.name} logged out.')
                break

    persistence.save_user(user)
    persistence.close()


if __name__ == '__main__':
    persistence = None # global
    main()