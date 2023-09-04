def sift_up(heap, index):
    if index == 1:
        return
    parent_index = index // 2
    if heap[parent_index] < heap[index]:
        heap[parent_index], heap[index] = heap[index], heap[parent_index]
        sift_up(heap, parent_index)


def heap_add(heap, key):
    index = len(heap)
    heap.append(key)
    sift_up(heap, index)
    return heap


def sift_down(heap, index):
    left = 2 * index 
    right = 2 * index + 1
    # нет дочерних узлов    
    if len(heap) - 1 < left:
        return
    # right <= heap.size проверяет, что есть оба дочерних узла
    if right <= len(heap) - 1 and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        sift_down(heap, index_largest) 

def pop_max(heap):
    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    sift_down(heap, 1)
    return result


heap = [None, 50, 45, 20, 17, 14, 10, 6, 5, 4]
print(heap_add(heap, 18))
pop_max(heap)
print(heap)

def heapsort(array):
    # Создадим пустую бинарную кучу.
    heap = [None]
  
    # Вставим в неё по одному все элементы массива сохраняя свойства кучи.
    for item in array:
        heap_add(heap, item)   # псевдокод для heap_add можно посмотреть в прошлом уроке
  
    # Будем извлекать из неё наиболее приоритетные элементы, удаляя их из кучи.
    sorted_array = []
    i = 0
    while len(heap) > 1:
        sorted_array.append(pop_max(heap))
        # псевдокод для heap_get_max_priority можно посмотреть в прошлом уроке
        i += 1

    return sorted_array

arr = [3, 5, 1, 6, 9, 2]

print(heapsort(arr))

