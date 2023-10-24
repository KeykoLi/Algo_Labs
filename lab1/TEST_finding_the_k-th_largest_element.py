import unittest

from finding_the_kth_largest_element import finding_the_kth_largest_element


class MyTestCase(unittest.TestCase):
    def test_k_less_than_zero(self):
        array_1 = [1, 2, 3, 4, 5]
        self.assertEqual(finding_the_kth_largest_element(array_1, 0), None)

    def test_k_larger_than_array_len(self):
        array_2 = [5, 4]
        self.assertEqual(finding_the_kth_largest_element(array_2, 6), None)

    def test_k_normal(self):
        array_3 = [4, 29, 10, 3, 5, 2, 0, 32]
        self.assertEqual(finding_the_kth_largest_element(array_3, 2), (29, 1))
