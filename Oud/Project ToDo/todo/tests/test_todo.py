import unittest

from ..models.todo import ToDo


class TestToDo(unittest.TestCase):
    """Test class for ToDo class"""

    def test_instantiation_required_argument(self):
        """Test if calling without arguments raises an error"""
        self.assertRaises(TypeError, ToDo)

    def test_instantiation(self):
        o = ToDo('note text')
        self.assertIsInstance(o, ToDo)

    def test_note(self):
        s = 'Boodschappen doen'
        o = ToDo(s)
        actual = o.note
        expected = s
        self.assertEqual(expected, actual)

    def test_prioriteit(self):
        value = 9
        o = ToDo('note text', prioriteit=value)
        expected = value
        actual = o.prioriteit
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
