def fibbonachi(n, k):
    if n <= 1:
        return 1
    result = [1, 1]
    i = 2
    mod = 10 ** k
    while i <= n:
        a = result[-1] + result[-2]
        b = result[-1]
        if a < mod:
            result[-1] = a
        else:
            result[-1] = a % mod
        result[-2] = b
        i += 1
    return result[-1]


number, k = input().strip().split()

print(fibbonachi(int(number), int(k)))
