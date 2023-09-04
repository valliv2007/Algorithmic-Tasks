n = int(input())
numbers = [int(x) for x in input().split()]
summary = 0
count = 0

for index, value in enumerate(numbers):
    summary += value - index
    if not summary:
        count += 1

print(count)
