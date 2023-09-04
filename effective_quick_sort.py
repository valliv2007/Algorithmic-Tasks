#  72861430

from typing import List, Optional, Tuple


class Contender:
    def __init__(self, login, score, penalty):
        self.login = login
        self.score = int(score)
        self.penalty = int(penalty)

    def __str__(self) -> str:
        return self.login

    def __lt__(self, other):
        return ((self.score, other.penalty, other.login)
                < (other.score, self.penalty, self.login))


def partition(array: List, start: int, end: Optional[int]) -> int:
    left = start
    pivot = array[end]
    for index in range(start, end):
        if pivot < array[index]:
            array[left], array[index] = array[index], array[left]
            left += 1
    array[left], array[end] = array[end], array[left]
    return left


def quicksort(array: List, start: int = 0,
              end: int = None, length: int = 0) -> List:
    if end is None:
        end = length - 1
    if start < end:
        mid = partition(array, start, end)
        quicksort(array, start, mid - 1)
        quicksort(array, mid + 1, end)
    return array


def read_input() -> Tuple[List, int]:
    num = int(input())
    contenders = [Contender(*input().split()) for _ in range(num)]
    return contenders, num


if __name__ == '__main__':
    array, amount = read_input()
    print(*quicksort(array, length=amount), sep='\n')
