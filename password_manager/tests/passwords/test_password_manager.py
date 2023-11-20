import string
import unittest

from password_manager.password_manager.passwords.password_generator import generate_password
from password_manager.password_manager.passwords.password_generator import InvalidArgumentException


class TestPasswordGenerator(unittest.TestCase):

    def test_lowercase_password(self):
        n = 8
        password = generate_password(n, n, 0, 0, 0)
        self.assertEqual(n, len(password))
        self.assertTrue(password.islower())

    def test_uppercase_password(self):
        n = 8
        password = generate_password(n, 0, n, 0, 0)
        self.assertEqual(n, len(password))
        self.assertTrue(password.isupper())

    def test_digits_password(self):
        n = 8
        password = generate_password(n, 0, 0, n, 0)
        self.assertEqual(n, len(password))
        self.assertTrue(password.isdigit())

    def test_special_password(self):
        n = 8
        password = generate_password(n, 0, 0, 0, n)
        self.assertEqual(n, len(password))
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_long_password(self):
        n = 20
        password = generate_password(n)
        self.assertEqual(n, len(password))

    def test_short_password(self):
        self.assertRaises(InvalidArgumentException, generate_password, 4, 2, 2, 1, 1)
