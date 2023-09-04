from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int, n, m) -> List[int]:
    # Здесь реализация вашего решения
    neighbors = []
    if row > 0:
        neighbors.append(matrix[row - 1][col])
    if col > 0:
        neighbors.append(matrix[row][col - 1])
    if row < n - 1:
        neighbors.append(matrix[row + 1][col])
    if col < m - 1:
        neighbors.append(matrix[row][col + 1])
    neighbors.sort()
    return neighbors

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m

matrix, row, col, n, m = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col, n, m))))