from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    # Здесь реализация вашего решения
    result = []
    cur_sum = sum(arr[:window_size])
    result.append(cur_sum / window_size)
    for index in range(0, len(arr)-window_size):
        cur_sum -= arr[index]
        cur_sum += arr[index + window_size]
        cur_avg = cur_sum / window_size
        result.append(cur_avg)
    return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))