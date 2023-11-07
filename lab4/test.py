import unittest

from lab4 import find_shortest_path, read_input_matrix


class MyTestCase(unittest.TestCase):
    def test_funct(self):
        test_matrix = [
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        ]

        # Збережемо тестову матрицю в файл "test_input.txt"
        with open("test_input.txt", "w") as file:
            for row in test_matrix:
                file.write("".join(map(str, row)) + "\n")

        # Запустимо алгоритм на тестових даних
        input_matrix = read_input_matrix("test_input.txt")
        shortest_path_length = find_shortest_path(input_matrix)
        self.assertEqual(shortest_path_length, 12)



