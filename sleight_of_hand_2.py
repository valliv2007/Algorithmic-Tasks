#  70937318
from collections import defaultdict
from typing import List, Tuple


def score_point(digits: List[str], number_fingers: int) -> int:
    players = 2
    players_fingers = number_fingers * players
    symbols = defaultdict(int)
    symbols_greater_fingers = set()
    points = 0
    for digit in digits:
        symbols[digit] += 1
        if symbols[digit] == 1:
            points += 1
        if symbols[digit] > players_fingers:
            symbols_greater_fingers.add(digit)
    return points - len(symbols_greater_fingers)


def read_input() -> Tuple[List[int], int]:
    number_fingers = int(input())
    digits = [digit for _ in range(4) for digit in input().replace('.', '')]
    return digits, number_fingers


if __name__ == '__main__':
    digits, number_fingers = read_input()
    print(score_point(digits, number_fingers))
