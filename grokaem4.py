n = [4, 6]

def sum(n):
    if not n:
        return 0
    return n[0] + sum(n[1:]) 

print(sum(n))

def length(n):
    if not n:
        return 0
    return 1 + length(n[1:])

print(length(n))

def max_numner(n):
    if not n:
        return 0
    max_n = n[0]
    if max_numner(n[1:]) > max_n:
        max_n = max_numner(n[1:])
    return max_n

print(max_numner(n))

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 6, 2, 25, 4, 38, 96, 6]))