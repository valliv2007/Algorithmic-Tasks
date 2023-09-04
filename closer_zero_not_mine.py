from typing import List

def get_nearest_zero(lane_length: int, lane: List[int]) -> int:
    result = [0] * lane_length
    lastzero = -lane_length
    for index in range(len(lane)):
        if lane[index]:
            result[index] = index - lastzero
        else:
            lastzero = index
    lastzero = 2 * lane_length
    for index in reversed(range(len(lane))):
        if lane[index]:
            result[index] = min(lastzero - index, result[index])
        else:
            lastzero = index
    return result


def read_input() -> List[int]:
    lane_length = int(input())
    lane = list(map(int, input().strip().split()))
    return lane_length, lane

if __name__ == '__main__':
    lane_length, lane = read_input()
    print(" ".join(map(str, get_nearest_zero(lane_length, lane))))