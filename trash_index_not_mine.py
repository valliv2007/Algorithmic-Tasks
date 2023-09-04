n = int(input())
L = [int(x) for x in input().split()]
k = int(input())

def enough(arr, diff, k, n):
    count, i, j = 0, 0, 0
    while i < n or j < n:
        while j < n and arr[j] - arr[i] <= diff:
            j += 1
        count += j - i - 1
        i += 1
    return count >= k
def kth_min_diff(arr, k, n):
    arr.sort()
    left, right = 0, arr[-1] - arr[0]
    while left < right:
        middle_diff = (left + right) // 2
        if not enough(arr, middle_diff, k, n):
            left = middle_diff + 1
        else:
            right = middle_diff
    return left
print(kth_min_diff(array, k, n))