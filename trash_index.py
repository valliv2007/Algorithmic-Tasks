n = int(input())
squares = [int(i)for i in input().split()]
k = int(input())
squares.sort(reverse=True)
result = []
count = 0
new_i = 0
new_j = 0

for i in range(n):
    if count < k:
        for j in range(i + 1, n):
            res = abs(squares[i] - squares[j])
            if count < k:
                result.append(res)
                count += 1
            else:
                new_j = j
                new_i = i
                break
    else:
        if not new_i:
            new_new_i = i
        break
result.sort()
answer = result[-1]
if new_j:
    for j in range(new_j, n):
        res = abs(squares[new_i] - squares[j])
        if res < answer:
            result.append(res)
            result.sort()
            result.pop()
            answer = result[-1]
if new_i:
    for i in range(new_i + 1, n):
        for j in range(i + 1, n):
            res = abs(squares[i] - squares[j])
            if res < answer:
                result.append(res)
                result.sort()
                result.pop()
                answer = result[-1]
else:
    for i in range(new_new_i, n):
        for j in range(i + 1, n):
            res = abs(squares[i] - squares[j])
            if res < answer:
                result.append(res)
                result.sort()
                result.pop()
                answer = result[-1]
print(result)
print(result[k - 1])
