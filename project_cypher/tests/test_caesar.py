import unittest

from project_cypher.cypher.caesar import Caesar


class TestCaesarCypher(unittest.TestCase):

    def test_instantiation(self):
        cypher = Caesar(3)
        self.assertIsInstance(cypher, Caesar)

    def test_encrypt(self):
        original = 'abcdefg'
        expected = 'DEFGHIJ'
        cypher = Caesar(3)
        encrypted = cypher.encrypt(original)
        self.assertIsInstance(encrypted, str)
        self.assertEqual(len(original), len(encrypted))
        self.assertTrue(encrypted.isupper())
        self.assertEqual(expected, encrypted)

    def test_decrypt(self):
        encrypted = 'EFGHIJK'
        expected = 'abcdefg'
        cypher = Caesar(4)
        decrypted = cypher.decrypt(encrypted)
        self.assertEqual(expected, decrypted)

    def test_encrypt_decrypt(self):
        original = 'abcdefg'
        cypher = Caesar(4)
        encrypted = cypher.encrypt(original)
        decrypted = cypher.decrypt(encrypted)
        self.assertEqual(original, decrypted)


if __name__ == '__main__':
    unittest.main()
