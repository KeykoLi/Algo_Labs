# Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином,
# щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.
#
# Нехай у вас задане бінарне дерево такого вигляду:
#
#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7
# Ваша функція має повернути дерево, яке виглядатиме наступним чином:
#
#     1
#    / \
#   3   2
#  / \ / \
# 7  6 5  4
# Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
#
# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value: int):
#         self.value = value
#         self.left = None
#         self.right = None
# Ваша функція має мати такий вигляд:
#
# def invert_binary_tree(tree) -> BinaryTree:
# Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з
# бінарного дерева.
# У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:
#
# root = BinaryTree(3)
# root.left = BinaryTree(9)
# root.right = BinaryTree(20)
# Ваша функція має повернути об'єкт класу BinaryTree.
# Для спрощення тестування даної функції достатньо реалізувати порівняння значень вузлів дерева
from collections import deque

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    # Рекурсивно інвертуємо лівий та правий піддерева
    left_sub = invert_binary_tree(tree.left)
    right_sub = invert_binary_tree(tree.right)

    # Міняємо місцями лівий та правий піддерева
    tree.left = right_sub
    tree.right = left_sub

    return tree


# def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
#     if tree is None:
#         return None
#
#     queue = deque()
#     queue.append(tree)
#
#     while queue:
#         current = queue.popleft()
#         current.left, current.right = current.right, current.left
#
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#
#     return tree
def print_binary_tree(tree: BinaryTree, level=0, prefix="Root: "):
    if tree is not None:
        if level == 0:
            print(f"{prefix}{tree.value}")
        else:
            indent = " " * (level * 4)
            print(f"{indent}{prefix}{tree.value}")

        print_binary_tree(tree.right, level + 1, "Right: ")
        print_binary_tree(tree.left, level + 1, "Left: ")


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print("Binary Tree:")
    print_binary_tree(root)

    inverted_tree = invert_binary_tree(root)

    print("Inverted Binary Tree:")
    print_binary_tree(inverted_tree)