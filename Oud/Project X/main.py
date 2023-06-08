from src.models.secret import Secret
from src.models.persistence import PersistenceWithPickle


def main_cli():

    username: str = input('Wie ben je? : ')

    options = {
        1: 'overzicht',
        2: 'geheim toevoegen',
        3: 'geheim opvragen',
        4: 'geheim verwijderen',
        9: 'exit'
    }

    try:
        secrets = PersistenceWithPickle.retrieve()
    except:
        secrets = []

    while True:
        print()
        for nr, text in options.items():
            print(nr, text)

        nr = int(input('Wat wil je doen? : '))

        match nr:
            case 1:
                print()
                for secret in secrets:
                    if secret.owner == username:
                        print(secret)

            case 2:
                secret_name: str = input('Welke geheim wil je opslaan? : ')
                secret_content: str = input('Wat is het geheim? : ')
                secret: Secret = Secret(secret_name, secret_content, username)
                secrets.append(secret)

            case 3:
                print()
                secret_name = input('Welke geheim wil je opvragen? : ')
                for secret in secrets:
                    if secret.name == secret_name and secret.owner == username:
                        print(f'{secret.name}: {secret.content}')
                        break
                else:
                    print('Kan dat geheim niet vinden.')

            case 4:
                print()
                secret_name = input('Welke geheim wil je verwijderen? : ')
                for i, secret in enumerate(secrets):
                    if secret.name == secret_name and secret.owner == username:
                        del secrets[i]
                        break
                else:
                    print('Kan dat geheim niet vinden.')

            case 9:
                print('Elvis has left the room.')
                break


    PersistenceWithPickle.store(secrets)


# ------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    main_cli()