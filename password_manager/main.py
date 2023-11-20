from password_manager.passwords.password_generator import generate_password
from password_manager.passwords.password_generator import InvalidArgumentException


def main():
    try:
        print('New password:', generate_password(8, 2, 2, 1, 1))

    except InvalidArgumentException as ex:
        print(ex)


if __name__ == '__main__':
    main()
