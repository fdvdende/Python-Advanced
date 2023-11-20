import random


class InvalidArgumentException(Exception):
    pass


def generate_password(required_length: int = 8,
                      n_lowercase: int = 1,
                      n_uppercase: int = 1,
                      n_numbers: int = 1,
                      n_special: int = 1) -> str:

    """A function to generate a secure password with minimal requirements"""

    lowercase_characters = 'abcdefghijkmnopqrstuvwxyz'  # removed l
    uppercase_characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # removed IO
    number_characters = '0123456789'
    special_characters = '@#$%&*+?!'

    n_extra = required_length - n_lowercase - n_uppercase - n_numbers - n_special

    if n_extra < 0:
        raise InvalidArgumentException('Required length is to low.')

    lower = random.choices(lowercase_characters, k=n_lowercase)
    upper = random.choices(uppercase_characters, k=n_uppercase)
    numbers = random.choices(number_characters, k=n_numbers)
    special = random.choices(special_characters, k=n_special)
    extra = random.choices(lowercase_characters +
                           uppercase_characters +
                           number_characters +
                           special_characters,
                           k=n_extra)

    all = lower + upper + numbers + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password


# -----------------------

if __name__ == '__main__':

    print(generate_password(8, 4, 4, 2, 0))