import unittest

from main import invert_binary_tree, BinaryTree


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_tree(self):

        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_tree = invert_binary_tree(root)

        self.assertEqual(inverted_tree.value, 1)
        self.assertEqual(inverted_tree.left.value, 3)
        self.assertEqual(inverted_tree.right.value, 2)
        self.assertEqual(inverted_tree.left.left.value, 7)
        self.assertEqual(inverted_tree.left.right.value, 6)
        self.assertEqual(inverted_tree.right.left.value, 5)
        self.assertEqual(inverted_tree.right.right.value, 4)


if __name__ == '__main__':
    unittest.main()