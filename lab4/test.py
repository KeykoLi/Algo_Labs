import unittest

from lab4 import converting_one_to_zero, check_and_change_zero_point,graph_from_matrix, shortest_path_graph


class MyTestCase(unittest.TestCase):
    def test_funct(self):
        test_matrix = [
            [0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1]
        ]
        matrix_t = converting_one_to_zero(test_matrix, check_and_change_zero_point)
        graph = graph_from_matrix(matrix_t)
        res = shortest_path_graph(graph, len(test_matrix[0]))

        self.assertEqual((7,1), res)



