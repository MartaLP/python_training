from unittest import TestCase
from d10.kalkulator import Kalk

class TestsKalk(TestCase):

    def setUp(self):
        self.kalk = Kalk()
        self.a = 5
        self.b = 4

    def test_dodaj(self):
        expected_sum = self.a + self.b
        actual_sum = self.kalk.dodaj(self.a, self.b)
        self.assertEqual(expected_sum, actual_sum)

    def test_odejmij(self):
        expected_min = self.a - self.b
        actual_min = self.kalk.odejmij(self.a, self.b)
        self.assertEqual(expected_min, actual_min)

    def test_pomnoz(self):
        expected = self.a * self.b
        actual = self.kalk.pomnoz(self.a, self.b)
        self.assertEqual(expected, actual)