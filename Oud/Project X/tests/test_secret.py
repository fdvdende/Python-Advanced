from src.models.secret import Secret

import unittest


class TestSecret(unittest.TestCase):

    def test_instantiation(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        self.assertIsInstance(secret, Secret)

    def test_str(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        s = str(secret)
        self.assertEqual(s[:6], 'Secret')

    def test_repr(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        s = repr(secret)
        self.assertRegex(s, 'Secret\(.*\)')

    def test_property_name(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        actual = secret.name
        expected = 'wachtwoord'
        self.assertEqual(expected, actual)

    def test_property_owner(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        actual = secret.owner
        expected = 'peter'
        self.assertEqual(expected, actual)

    def test_property_secret(self):
        secret = Secret('wachtwoord', 'Welkom2023!', 'peter')
        actual = secret.content
        expected = 'Welkom2023!'
        self.assertEqual(expected, actual)
