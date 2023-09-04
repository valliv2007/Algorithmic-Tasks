from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    # Здесь реализация вашего решения
    number_list.reverse()
    first_number = 0
    for i in range(len(number_list)):
        first_number += int(number_list[i]) * (10 ** i)
    result = first_number + k
    return [n for n in str(result)]


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
