import unittest

from src.main import build_trie


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.patterns = ["some", "small", "banana", "big", "biathlon"]
        self.trie = build_trie(self.patterns)

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("some"))

    def test_search_nonexistent_word(self):
        self.assertFalse(self.trie.search("orange"))

    def test_starts_with_prefix_existing_prefix(self):
        self.assertTrue(self.trie.search_prefix("ban"))

    def test_starts_with_prefix_nonexistent_prefix(self):
        self.assertFalse(self.trie.search_prefix("xyz"))

    def test_insert_and_search_new_word(self):
        new_word = "abc"
        self.assertFalse(self.trie.search(new_word))
        self.trie.insert(new_word)
        self.assertTrue(self.trie.search(new_word))


if __name__ == '__main__':
    unittest.main()
