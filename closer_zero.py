import timeit
from typing import List


def get_sum(houses_numbers: List[int]) -> List[int]:
    distances_to_zero = []
    is_next_zero = True
    for i in range(len(houses_numbers)):
        if houses_numbers[i] == 0:
            first_zero = i
            break
    next_zero = first_zero
    for i in range(len(houses_numbers)):
        if is_next_zero and i > first_zero and i > next_zero:
            first_zero = next_zero
            for j in range(i, len(houses_numbers)):
                if houses_numbers[j] == 0:
                    next_zero = j
                    if next_zero - i >= i - first_zero:
                        distances_to_zero.append(abs(i - first_zero))
                    else:
                        distances_to_zero.append(next_zero - i)
                    is_next_zero = True
                    break
                else:
                    is_next_zero = False
            if not is_next_zero:
                distances_to_zero.append(abs(i - first_zero))
        else:
            if next_zero - i >= i - first_zero:
                distances_to_zero.append(abs(i - first_zero))
            else:
                distances_to_zero.append(abs(next_zero - i))
    return distances_to_zero


def read_input() -> List[int]:
    n = int(input())
    houses_numbers = list(map(int, input().strip().split()))
    return houses_numbers


print(" ".join(map(str, get_sum(read_input()))))

def get_sum_1(houses_numbers):
    distances_to_zero = []
    is_next_zero = True
    for i in range(len(houses_numbers)):
        if houses_numbers[i] == 0:
            closer_zero = i
            break
    for i in range(len(houses_numbers)):
        if is_next_zero and i > closer_zero:
            for j in range(i, len(houses_numbers)):
                if houses_numbers[j] == 0:
                    if j - i >= i - closer_zero:
                        distances_to_zero.append(abs(i - closer_zero))
                    else:
                        distances_to_zero.append(j - i)
                        closer_zero = j
                    is_next_zero = True
                    break
                else:
                    is_next_zero = False
            if not is_next_zero:
                distances_to_zero.append(abs(i - closer_zero))
        else:
            distances_to_zero.append(abs(i - closer_zero))

    return distances_to_zero


str_1 = '1 2 3 4 0 5 6 7 0 8 9 5 0 4 6 7 8 9 2 4 7 3 6 8 9' * 10000
num_1 = list(map(int, str_1.strip().split()))
print(timeit.timeit('get_sum(num_1)', setup='from __main__ import get_sum, num_1', number=2))
print(timeit.timeit('get_sum_1(num_1)', setup='from __main__ import get_sum_1, num_1', number=2))