import unittest

from help_gorilla import eat_bananas


class MyTestCase(unittest.TestCase):
    def test_array_have_zero(self):
        piles_1 = [2, 3, 0]
        self.assertEqual(eat_bananas(piles_1, 3), None)

    def test_len_array_largest_than_time(self):
        piles_2 = [2, 3, 1, 4, 3]
        self.assertEqual(eat_bananas(piles_2, 3), None)

    def test_right_conditions(self):
        piles_3 = [2, 3, 4, 5, 1]
        self.assertEqual(eat_bananas(piles_3, 8), 3)