n = int(input())
lengths = [int(i)for i in input().split()]
lengths.sort(reverse=True)
for i in range(n):
    if lengths[i] < lengths[i + 1] + lengths[i + 2]:
        perimeter = lengths[i] + lengths[i + 1] + lengths[i + 2]
        break

print(perimeter)
