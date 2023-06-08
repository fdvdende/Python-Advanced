from src.models.encryption import Encryption

import unittest


class TestSecret(unittest.TestCase):

    def test_encrypt(self):
        message = 'André'

        encrypted = Encryption.encrypt(message)
        decrypted = Encryption.decrypt(encrypted)

        self.assertEqual(message, decrypted)
