from project_c.models.user import User
from project_c.models import exceptions
from project_c.models.persistence import Persistence


def menu():
    options = {
        1: 'Overzicht van gebruikers',
        2: 'Gebruiker toevoegen',
        3: 'Gebruiker verwijderen',
        4: 'Stoppen',
    }

    menu = '\nMogelijke acties:\n' + '\n'.join(f'{k}) {v}' for k, v in options.items())

    while True:
        try:
            print(menu)
            choice = int(input('Wat wil je doen? '))
            if 1 <= choice <= len(menu):   # choice >= 1 and choice <= 4
                print()
                return choice
            else:
                assert False, 'Illegal.'
        except:
            print('Probeer nogmaals.')


def main():

    persistence = Persistence()

    while True:
        choice = menu()

        match choice:

            case 1:
                user_names = persistence.get_user_names()
                if len(user_names) == 0:
                    print('Geen gebruikers.')
                else:
                    print('Gebruikers:')
                    for user_name in user_names:
                        print(user_name)

            case 2:
                user_name = input('Geef naam van de gebruiker die je wilt toevoegen: ')
                user_password = input('Geef initiële wachtwoord: ')

                user = User(user_name)
                try:
                    user.set_password(user_password)
                except exceptions.InvalidPasswordException:
                    print('Dat wachtwoord voldoet niet aan de eisen.')
                    continue

                persistence.save_user(user)
                print('Gebruiker is toegevoegd.')

            case 3:
                user_name = input('Geef naam van de gebruiker die je wilt verwijderen: ')

                persistence.remove_user(user_name)
                print('Gebruiker is verwijderd.')

            case 4:
                break

    persistence.close()


if __name__ == '__main__':
    main()