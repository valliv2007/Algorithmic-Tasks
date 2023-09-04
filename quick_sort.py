def partition(array, pivot):
    left = []
    center = []
    right = []
    for elem in array:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            center.append(elem)
        else:
            right.append(elem)
    return left, center, right


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array    # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[0]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


print(quicksort([25, 755, -40, 57, -41]))
