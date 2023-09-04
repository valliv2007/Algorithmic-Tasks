from collections import defaultdict

n = int(input())
participants = [int(i)for i in input().split()]
k = int(input())
univercities = defaultdict(int)

for participant in participants:
    univercities[participant] += 1
sorted_tuples = sorted(univercities.items(), key=lambda item: item[1], reverse=True)
sort_univercities = {k: v for k, v in sorted_tuples}
keys = list(sort_univercities)
result = []
for i in range(k):
    result.append(keys[i])

print(*result)
