n = int(input())
m = int(input())
new_rows = []
for _ in range(m):
    new_rows.append([])
for i in range(n):
    row = input().split()
    for j in range(m):
        new_rows[j].append(row[j])

for row in new_rows:
    print(*row, sep=' ')
