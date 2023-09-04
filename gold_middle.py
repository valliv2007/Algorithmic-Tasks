n = int(input())
m = int(input())
north = [int(i)for i in input().split()]
south = [int(i)for i in input().split()]
length = n + m
result = [None] * length
x, r, k = 0, 0, 0
while x < n and r < m:
    if north[x] <= south[r]:
        result[k] = north[x]
        x += 1
    else:
        result[k] = south[r]
        r += 1
    k += 1
while x < n:
    result[k] = north[x]
    x += 1
    k += 1
while r < m:
    result[k] = south[r]
    r += 1
    k += 1
if length % 2 == 0:
    i = int(length / 2)
    res = (result[i - 1] + result[i]) / 2
    if res % 1 == 0.0:
        print(int(res))
    else:
        print(res)
else:
    print(result[length // 2])
