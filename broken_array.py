# 72814500

from typing import List


def binary_search(arr: List, target: int, left: int, right: int) -> int:
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid)
    else:
        return binary_search(arr, target, mid + 1, right)


def broken_search(nums: List, target: int) -> int:
    first = 0
    last = len(nums) - 1
    while first < last:
        correct_first = first + (last - first) // 2
        if nums[correct_first] > nums[last]:
            first = correct_first + 1
        else:
            last = correct_first
    left = 0
    right = len(nums) - 1
    if nums[first] <= target <= nums[right]:
        left = first
    else:
        right = first - 1
    return binary_search(nums, target, left, right + 1)


if __name__ == '__main__':
    _ = input()
    target = int(input())
    nums = [int(elem) for elem in input().split()]
    print(broken_search(nums, target))
