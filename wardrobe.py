def counting_sort(array, k=3):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(counted_values[value]):
            array[index] = value
            index += 1

n = int(input())
clothes = [int(i) for i in input().split()]
counting_sort(clothes)
print(" ".join(map(str, clothes)))