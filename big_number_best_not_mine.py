def sort_buble(unsorted):
    count = 1
    while count > 0:
        count = 0
        for i in range(len(unsorted)-1):
            first = unsorted[i] + unsorted[i+1]
            second = unsorted[i+1] + unsorted[i]
            if first < second:
                unsorted[i], unsorted[i+1] = unsorted[i + 1], unsorted[i]
                count += 1

    return unsorted
n = int(input())
numbers = input().strip().split()

print(*sort_buble(numbers))