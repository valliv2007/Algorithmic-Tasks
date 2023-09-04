#  70936893
from typing import List


def get_sum(houses_numbers: List[int], street_length: int) -> List[int]:
    distances_to_zero = [0 for _ in range(street_length)]
    left_zero = -1
    for index, number in enumerate(houses_numbers):
        if number == 0:
            if index != 0:
                for distance_index in range(left_zero + 1, index):
                    distance_to_right = index - distance_index
                    distance_to_left = distance_index - left_zero
                    if left_zero < 0 or distance_to_right <= distance_to_left:
                        distances_to_zero[distance_index] = distance_to_right
                    else:
                        distances_to_zero[distance_index] = distance_to_left
            left_zero = index
    for reverse_index in range(left_zero + 1, street_length):
        distances_to_zero[reverse_index] = reverse_index - left_zero
    return distances_to_zero


def read_input() -> List[int]:
    street_length = int(input())
    houses_numbers = [int(number) for number in input().strip().split()]
    return houses_numbers, street_length


if __name__ == '__main__':
    houses_numbers, street_length = read_input()
    print(*get_sum(houses_numbers, street_length))
