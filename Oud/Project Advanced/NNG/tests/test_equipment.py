import unittest

from modelsX.equipment import Equipment
from modelsX.materiaal import Materiaal

class EqupimentTests(unittest.TestCase):

    def test_upper1(self):
        s = 'abcdefg'
        actual = s.upper()
        expected = 'ABCDEFG'
        self.assertEqual(expected, actual)

    def test_upper2(self):
        s = 'abcdefg'
        actual = s.upper()
        expected = 'ABCDEF'
        self.assertNotEqual(expected, actual)

    def test_add_float1(self):
        actual = 0.1 + 0.2
        expected = 0.3
        self.assertAlmostEqual(expected, actual)

    def test_instatiation(self):
        equipment = Equipment()
        self.assertIsNotNone(equipment)
        self.assertIsInstance(equipment, Equipment)
        self.assertIsInstance(equipment.equipment, list)
        self.assertEqual(0, len(equipment.equipment))

    def test_add_material(self):
        equipment = Equipment()
        materiaal = Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front')
        equipment.add_materiaal(materiaal)
        self.assertNotEqual(0, len(equipment.equipment))

    def test_get_material(self):
        equipment = Equipment()
        materiaal = Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front')
        equipment.add_materiaal(materiaal)
        materiaal_opgehaald = equipment.get_materiaal('374589-324678')
        self.assertIsNotNone(materiaal_opgehaald)

    def test_materiaal_str(self):
        materiaal = Materiaal('A', 'B', 'C', 'D', 'E', 'F', 'G')
        s = repr(materiaal)
        self.assertTrue(s.startswith('A - B - C - D - E - F - G'))
