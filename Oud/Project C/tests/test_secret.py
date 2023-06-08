from project_c.models.secret import Secret

import unittest


class TestSecret(unittest.TestCase):

    def setUp(self):
        self.name = 'My password'
        self.content = 'abc'
        self.secret = Secret(self.name, content = self.content)

    def tearDown(self):
        pass

    def test_instantiation(self):
        self.assertIsInstance(self.secret, Secret)

    def test_secret_str(self):
        actual = str(self.secret)
        expected = 'Secret: ' + self.name
        self.assertEqual(expected, actual)

    def test_secret_repr(self):
        actual = repr(self.secret)
        expected = f'Secret("{self.name}", ...)'
        self.assertEqual(expected, actual)
        self.assertRegex(actual, f'Secret.*{self.name}.*')

