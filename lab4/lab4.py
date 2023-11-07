from collections import deque

# Функція для зчитування матриці з файлу
def read_input_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(cell) for cell in line.strip()]
            matrix.append(row)
    return matrix


# Функція для знаходження найкоротшого шляху за допомогою BFS
def find_shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # Ініціалізуємо чергу для BFS та матрицю відстаней
    queue = deque([(i, 0) for i in range(rows) if matrix[i][0] == 1])
    distance = [[-1] * cols for _ in range(rows)]

    while queue:
        x, y = queue.popleft()
        # Якщо поточна клітинка знаходиться в останньому стовпці, то шлях знайдено
        if y == cols - 1:
            return distance[x][y] + 1
        # Перевірка всіх можливих напрямків руху
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            # Перевірка чи нова клітинка знаходиться в межах матриці та є доступною
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    # Якщо шлях не знайдено, повернути -1
    return -1

# Функція для запису результату у файл
def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    input_matrix = read_input_matrix("input.txt")
    shortest_path_length = find_shortest_path(input_matrix)
    write_output("output.txt", shortest_path_length)
