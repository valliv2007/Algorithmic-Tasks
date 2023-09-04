kids = input()
factors = [int(i)for i in input().split()]
cookies = input()
sizes = [int(i)for i in input().split()]

count = 0
factors.sort()
sizes.sort()
index = -1
for factor in factors:
    for i in range(index + 1, len(sizes)):
        if sizes[i] >= factor:
            count += 1
            index = i
            break

print(count)
