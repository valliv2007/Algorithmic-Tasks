from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Здесь реализация вашего решения
    numbers = set()
    for first_number in arr:
        second_number = target_sum - first_number
        if second_number in numbers:
                return first_number, second_number
        else:
            numbers.add(first_number)
    return None

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))