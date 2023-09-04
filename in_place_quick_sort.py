def partition(array, pivot):
    left = 0
    right = len(array) - 1
    while left < right:
        while array[left] < pivot and left < right:
            left += 1
        while array[right] > pivot and left < right:
            right -= 1
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return left if left > 1 else 1
   

def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array    # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[len(array) // 2]
        divider = partition(array, pivot)
        if divider == len(array):
            divider -= 1
        return quicksort(array[:divider]) + quicksort(array[divider:])


print(quicksort(['que', 'bdfdcd', 'aaaa', 'quaas', 'bad']))