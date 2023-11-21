from collections import defaultdict

def find_unreachable_cities(storages, cities, pipelines):
    graph = build_graph(pipelines)
    unreachable_cities = []

    for storage in storages:
        remaining_cities = remove_connected_cities(graph.copy(), storage, cities)
        if remaining_cities:
            unreachable_cities.append([storage, remaining_cities])

    return unreachable_cities

def build_graph(pipelines):
    graph = defaultdict(list)
    for pipeline in pipelines:
        graph[pipeline[0]].append(pipeline[1])
    return graph

def remove_connected_cities(graph, storage_point, cities):
    if storage_point in graph:
        connected_cities = dfs(graph, storage_point)
        remaining_cities = list(set(cities) - set(connected_cities))
        return remaining_cities
    else:
        return cities

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        current_city = stack.pop()
        if current_city not in visited:
            visited.add(current_city)
            stack.extend(set(graph[current_city]) - visited)

    return visited

cities = ['Львів', 'Стрий', 'Долина']
storages = ['Сховище_1', 'Сховище_2']
pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]

result = find_unreachable_cities(storages, cities, pipelines)
print(result)
