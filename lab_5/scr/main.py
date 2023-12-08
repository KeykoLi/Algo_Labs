from collections import defaultdict


def find_unreachable_cities(storages, cities, pipelines):
    """
    Знаходить недосяжні міста для кожного сховища.

    Параметри:
    - storages: список сховищ
    - cities: список міст
    - pipelines: список активних газопроводів

    Повертає:
    Список недосяжних міст для кожного сховища у форматі [сховище, [місто_1, місто_2, ...]]
    """
    graph = build_graph(pipelines)
    unreachable_cities = []

    for storage in storages:
        remaining_cities = remove_connected_cities(graph.copy(), storage, cities)
        if remaining_cities:
            unreachable_cities.append([storage, remaining_cities])

    return unreachable_cities


def build_graph(pipelines):
    """
    Побудова графа зі списку активних газопроводів.

    Параметри:
    - pipelines: список активних газопроводів у форматі [['місто_1', 'місто_2'], ...]

    Повертає:
    Словник, де ключі - початкові міста газопроводів, значення - списки кінцевих міст.
    """
    graph = defaultdict(list)
    for pipeline in pipelines:
        graph[pipeline[0]].append(pipeline[1])
    return graph


def remove_connected_cities(graph, storage_point, cities):
    """
    Видаляє з'єднані міста та повертає залишкові міста.

    Параметри:
    - graph: граф газопроводів
    - storage_point: сховище, від якого починається пошук
    - cities: список всіх міст

    Повертає:
    Список залишкових міст після видалення з'єднаних міст.
    """
    if storage_point in graph:
        remaining_cities = dfs(graph, storage_point, cities)
        return remaining_cities
    else:
        return cities


def dfs(graph, start, cities):
    """
    Реалізує глибинний пошук в графі.

    Параметри:
    - graph: граф газопроводів
    - start: місто, з якого починається пошук
    - cities: список всіх міст

    Повертає:
    Список міст, які залишились після глибинного пошуку.
    """
    visited = set()
    stack = [start]

    while stack:
        current_city = stack.pop()
        if current_city not in visited:
            visited.add(current_city)
            stack.extend(set(graph[current_city]) - visited)

    remaining_cities = list(set(cities) - visited)
    return remaining_cities


def read_file(filename):
    #Зчитує дані з файлу.

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()
        cities = data[0].strip().split()
        storages = data[1].strip().split()
        pipelines = [line.strip().split() for line in data[2:]]
    return cities, storages, pipelines


def write_to_file(filename, result):
    #Записує результат у файл

    with open(filename, 'w', encoding='utf-8') as file:
        for item in result:
            file.write(str(item) + '\n')


if __name__ == "__main__":

    cities, storages, pipelines = read_file('input.txt')
    print(cities)
    print(storages)
    print(pipelines)
    result = find_unreachable_cities(storages, cities, pipelines)
    print(result)
    write_to_file('output.txt', result)
