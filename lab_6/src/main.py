class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def print_trie(self, node=None, level=0):
        if node is None:
            node = self.root

        if not node.children:
            return

        indentation = "  " * level
        for char, child in node.children.items():
            print(f"{indentation}{char}")
            self.print_trie(child, level + 1)

    def search_with_prefix(self, prefix):
        node = self.root
        result = []

        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]

        self.find_words_with_prefix(node, prefix, result)
        return result

    def find_words_with_prefix(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)

        for char, child in node.children.items():
            self.find_words_with_prefix(child, prefix + char, result)

def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

patterns = ["some", "banana", "big", "bigger", "bidhgfh", "bib"]
trie = build_trie(patterns)

trie.insert("small")
trie.insert("biathlon")

trie.print_trie()
print(trie.search_prefix("bia"))
print(trie.search("small"))

print(trie.search_with_prefix("bi"))





