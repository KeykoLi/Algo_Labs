import unittest

from main import find_unreachable_cities


class MyTestCase(unittest.TestCase):
    def test_function_all_connected(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'], ['Сховище_2', 'Долина']]

        result = find_unreachable_cities(storage, cities, pipelines)
        self.assertEqual([], result)


    def test_no_connection(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = []

        result = find_unreachable_cities(storage, cities, pipelines)
        expected_result = [['Сховище_1', ['Львів', 'Стрий', 'Долина']], ['Сховище_2', ['Львів', 'Стрий', 'Долина']]]
        self.assertEqual(result, expected_result)

    def test_one_storage_without_connections(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'], ['Сховище_1', 'Долина']]

        result = find_unreachable_cities(storage, cities, pipelines)
        expected_result = [['Сховище_2', ['Львів', 'Стрий', 'Долина']]]
        self.assertEqual(result, expected_result)
