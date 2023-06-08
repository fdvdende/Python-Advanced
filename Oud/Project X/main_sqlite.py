import logging

from src.models.secret import Secret
from src.models.persistence import PersistenceWithSQLite

import logging

logging.basicConfig(filename = 'secrets.log', # or to a file 'example.log',
                    level = logging.DEBUG,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%Y-%m-%dT%H:%M:%S')


def main_cli():

    username: str = input('Wie ben je? : ')

    options = {
        1: 'overzicht',
        2: 'geheim toevoegen',
        3: 'geheim opvragen',
        4: 'geheim verwijderen',
        9: 'exit'
    }

    while True:
        print()
        for nr, text in options.items():
            print(nr, text)

        nr = int(input('Wat wil je doen? : '))

        match nr:
            case 1:
                logging.info('overzicht')
                print()
                for secret in PersistenceWithSQLite.get_secrets():
                    if secret.owner == username:
                        print(secret)

            case 2:
                logging.info('toevoegen')
                print()
                secret_name: str = input('Welke geheim wil je opslaan? : ')
                secret_content: str = input('Wat is het geheim? : ')
                secret: Secret = Secret(secret_name, secret_content, username)
                PersistenceWithSQLite.store_secret(secret)

            case 3:
                logging.info('opvragen')
                print()
                secret_name = input('Welke geheim wil je opvragen? : ')
                for secret in PersistenceWithSQLite.get_secrets():
                    if secret.name == secret_name and secret.owner == username:
                        print(f'{secret.name}: {secret.content}')
                        break
                else:
                    print('Kan dat geheim niet vinden.')

            case 4:
                logging.info('delete')
                print()
                secret_name = input('Welke geheim wil je verwijderen? : ')
                PersistenceWithSQLite.delete_secret(secret_name, username)

            case 9:
                print('Elvis has left the room.')
                break




# ------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    main_cli()