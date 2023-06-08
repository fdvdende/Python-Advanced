from project_c.models.user import User
from project_c.models.exceptions import *

import unittest


class TestUser(unittest.TestCase):

    def test_instantiation(self):
        user = User('Peter')
        self.assertIsInstance(user, User)

    def test_user_str(self):
        name = 'Peter'
        user = User(name)
        actual = str(user)
        expected = 'User: ' + name
        self.assertEqual(expected, actual)

    def test_user_repr(self):
        # AAA - Arrange - Act - Assert

        # Arrange
        name = 'Peter'
        user = User(name)

        # Act
        actual = repr(user)

        # Assert
        expected = f'User("{name}")'
        self.assertEqual(expected, actual)

        self.assertRegex(actual, f'User.*{name}.*')

    def test_user_set_invalid_password(self):
        name = 'Peter'
        user = User(name)

        def set_password():
            nonlocal user
            password = 'abcA'
            user.set_password(password)

        self.assertRaises(InvalidPasswordException, set_password)


    def test_user_set_and_check_password(self):
        name = 'Peter'
        user = User(name)

        password = 'abcABC1!'
        user.set_password(password)

        self.assertTrue(user.check_password(password))

    def test_user_name(self):
        name = 'Peter'
        user = User(name)
        self.assertEqual(name, user.name)

    def test_user_name_read_only(self):
        name = 'Peter'
        user = User(name)

        def assign_user_name():
            nonlocal user
            user.name = 'xxx'

        self.assertRaises(AttributeError, assign_user_name)
