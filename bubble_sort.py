n = int(input())
s = input()
numbers = [int(i) for i in s.split()]
control = [int(i) for i in s.split()]

for i in range(n - 1):
    a = numbers[:n - i - 1]
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    if numbers[:n - i - 1] != a:
        print(*numbers, sep=' ')


if control == numbers:
    print(*numbers, sep=' ')
