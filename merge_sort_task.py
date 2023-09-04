def merge(arr, lf, mid, rg):
    result = [None] * len(arr)
    l, r, k = 0, 0, 0
    left = arr[lf: mid]
    right = arr[mid: rg]
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def merge_sort(arr, lf, rg):
    mid = int((lf + rg) / 2)
    left = arr[lf: mid]
    right = arr[mid: rg]
    left.sort()
    right.sort()
    new_arr = left + right
    result = merge(new_arr, 0, int(len(new_arr) / 2), len(new_arr))
    for i in range(lf, rg):
        arr[i] = result[i - lf]


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

test()