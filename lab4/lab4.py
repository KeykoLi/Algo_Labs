from queue import Queue

def is_valid(x, y, columns, rows):
    # Перевіряє, чи координати (x, y) знаходяться в межах матриці MxN
    return 0 <= x < columns and 0 <= y < rows

def converting_one_to_zero(matrix, update_condition):
    columns, rows = len(matrix), len(matrix[0])
    # Використовуємо вказану умову для заміни значень у копії матриці
    matrix_copy = [[update_condition(matrix, x, y, columns, rows) for y in range(rows)] for x in range(columns)]
    return matrix_copy

def check_and_change_zero_point(matrix, x, y, columns, rows):
    # Перевіряє, чи є сусід зі значенням 0, якщо так - повертає 0, в іншому випадку - поточне значення матриці
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, columns, rows) and matrix[new_x][new_y] == 0:
                return 0
    return matrix[x][y]

def graph_from_matrix(matrix):
    columns, rows = len(matrix), len(matrix[0])
    graph = {}

    for i in range(columns):
        for j in range(rows):
            if matrix[i][j] == 1:
                # Створює список сусідів для кожної одиниці у матриці
                neighbors = [(ni, nj) for ni, nj in [(i + dx, j + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]] if
                             is_valid(ni, nj, columns, rows) and matrix[ni][nj] == 1]
                graph[(i, j)] = neighbors
    return graph

def is_not_fully_zero(matrix):
    rows = len(matrix)
    first_column = [matrix[i][0] for i in range(rows)]
    last_column = [matrix[i][-1] for i in range(rows)]

    # Перевірка першого стовпця
    if all(value == 0 for value in first_column):
        if all (value == 0 for value in last_column):
            return False
        else:
            return True
    else:
        return True

def bfs(graph, start, target_column):
    queue = Queue()
    visited = set()
    parent_map = {}

    #починаємо з стартової вершини, додаємо її до черги та відзначаємо як відвідану
    queue.put((start, 0))
    visited.add(start)

    while not queue.empty():
        current_node, distance = queue.get()

        if current_node[1] == target_column:
            # Відтворюємо шлях від кінцевої вершини до початкової
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = parent_map.get(current_node)
            return distance, path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.put((neighbor, distance + 1))
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    return -1, []

def shortest_path_graph(graph, m, matrix):
    check_zero = is_not_fully_zero(matrix)
    if check_zero == True:
        return -1
    counter = 0
    def bfs_w(node):
        # Збільшуємо лічильник при кожному виклику BFS
        nonlocal counter
        counter += 1
        return bfs(graph, node, m - 1)

    min_path_len = float('inf')
    min_path = []

    for node in graph:
        if node[1] == 0:
            # Знаходимо найкоротший шлях для кожної вершини, що знаходиться у першому стовпці
            path_len, path = bfs_w(node)
            if path_len != -1:
                # Оновлюємо мінімальну довжину та маршрут, якщо поточний шлях коротший
                if path_len < min_path_len:
                    min_path_len = path_len
                    min_path = path

        if min_path == m - 1:
            # Якщо знайдено шлях до кінцевої вершини, завершуємо виконання
            return min_path_len, counter

    return (min_path_len, counter, min_path) if min_path_len != float('inf') else (-1, counter)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        matrix = []
        for line in f.readlines():
            # Зчитуємо вхідний файл і формуємо матрицю
            row = [int(i) for i in line.split()]
            matrix.append(row)
    matrix = converting_one_to_zero(matrix, check_and_change_zero_point)
    graph = graph_from_matrix(matrix)
    res = shortest_path_graph(graph, len(matrix[0]), matrix)

    with open("output.txt", "w") as f:
        # Записуємо результат у вихідний файл
        f.write(str(res))
