#  70838615
from typing import List, Tuple


def score_point(numbers: List[int], k: int) -> int:
    point = 0
    players = 2
    symbols = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0}
    for number in numbers:
        symbols[number] += 1
    for symbol in symbols:
        if 0 < symbols[symbol] <= k * players:
            point += 1
    return point


def read_input() -> Tuple[List[int], int]:
    k = int(input())
    numbers = list((input() + input() + input() + input()).replace('.', ''))
    return numbers, k


numbers, k = read_input()
print(score_point(numbers, k))
