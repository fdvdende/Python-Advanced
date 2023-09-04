from cypher import Cypher

from string import ascii_lowercase, digits, punctuation


class Caesar(Cypher):

    alphabet = ascii_lowercase + digits + punctuation

    def __init__(self, shift = 3):
        self._shift = shift

    def encrypt(self, original):
        substitution = Caesar.alphabet[self._shift:] + Caesar.alphabet[:self._shift]
        d = dict(zip(Caesar.alphabet, substitution.upper()))
        encrypted = ''.join(d.get(c, c) for c in original.lower())
        return encrypted

    def decrypt(self, encrypted):
        substitution = Caesar.alphabet[self._shift:] + Caesar.alphabet[:self._shift]
        d = dict(zip(substitution.upper(), Caesar.alphabet))
        original = ''.join(d.get(c, c) for c in encrypted.upper())
        return original


# ------------------------------------------------

if __name__ == '__main__':

    original = input('Geef tekst: ')

    cypher = Caesar(3)
    encrypted = cypher.encrypt(original)

    print('Encryped: ', encrypted)

    decrypted = cypher.decrypt(encrypted)

    print('Decryped: ', decrypted)

    assert decrypted == original
    print('Everything seems OK!')
