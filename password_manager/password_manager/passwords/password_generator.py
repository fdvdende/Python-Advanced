import random


class InvalidArgumentException(Exception):
    pass


def generate_password(required_length=8,
                      n_lowercase=1,
                      n_uppercase=1,
                      n_numbers=1,
                      n_special=1):

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

    print(generate_password(8, 4, 4, 0, 0))