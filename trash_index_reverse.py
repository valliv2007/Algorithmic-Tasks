n = int(input())
squares = [int(i)for i in input().split()]
k = int(input())


def is_more(array, difference, n, k):
    count, i, j = 0, 0, 0
    while i < n or j < n:
        while j < n and array[j] - array[i] <= difference:
            j += 1
        count += j - i - 1
        i += 1
    return count >= k


squares.sort()
left = 0
right = squares[-1] - squares[0]
while left < right:
    middle_differnce = (left + right) // 2
    if is_more(squares, middle_differnce, n, k):
        right = middle_differnce
    else:
        left = middle_differnce + 1

print(left)
