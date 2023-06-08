from project_c.models.encryption import get_hash, encrypt, decrypt

import string
import random
import unittest
import string


class TestEncryption(unittest.TestCase):

    def setUp(self):
        k = random.randint(32, 128)
        self.text = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k = k))

    def test_get_hash(self):
        generated_hash = get_hash(self.text)
        self.assertIsInstance(generated_hash, str)
        self.assertGreaterEqual(len(generated_hash), 10)

    def test_encryption(self):
        encrypted = encrypt(self.text)
        decrypted = decrypt(encrypted)
        self.assertEqual(self.text, decrypted)
