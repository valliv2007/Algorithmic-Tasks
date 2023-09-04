class Node:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = height


def small_left_rotation(a):
    # Задаём обозначения.
    b = a.right
    C = b.left
    R = b.right

    # Переусыновляем вершины.
    a.right = C
    b.left = a

    # Корректируем высоты в зависимости от того, равны ли высоты C и R.
    if C.height == R.height:
        a.height -= 1
        b.height += 1
    else:
        a.height -= 2

    # Возвращаем новый корень.
    return b

def small_right_rotation(a):
    # Задаём обозначения.
    b = a.left
    C = b.right
    L = b.left

    # Переусыновляем вершины.
    a.left = C
    b.right = a

    # Корректируем высоты в зависимости от того, равны ли высоты C и L.
    if C.height == L.height:
        a.height -= 1
        b.height += 1
    else:
        a.height -= 2

    # Возвращаем новый корень.
    return b

def big_left_rotation(a):
    # Задаём обозначения.
    b = a.right
    c = b.left
    M = c.left
    N = c.right

    # Переусыновляем вершины.
    a.right = M
    b.left = N
    c.left = a
    c.right = b

    # Корректируем высоты.
    a.height -= 2
    b.height -= 1
    c.height += 1

    # Возвращаем новый корень.
    return c

def big_left_rotation_short(v):
    # Правым ребёнком становится новый корень правого поддерева.
    v.right = small_right_rotation(v.right)
    # Возвращаем новый корень поддерева.
    return small_left_rotation(v)

def big_right_rotation_short(v):
    # Левым ребёнком становится новый корень левого поддерева.
    v.left = small_left_rotation(v.left)
    # Возвращаем новый корень поддерева.
    return small_right_rotation(v)

def rotate(vertex):
    if abs(vertex.left.height - vertex.right.height) < 2:
        # Вращать не надо, поддерево с вершиной vertex и так сбалансировано.
        return vertex
    if vertex.left.height - vertex.right.height == -2:
        # Нам нужны левые вращения.
        b = vertex.right
        R = b.right
        C = b.left

        if C.height <= R.height:
            # Нужно малое левое вращение.
            return small_left_rotation(vertex)
        else:
            # Нужно большое левое вращение.
            return big_left_rotation_short(vertex)

    if vertex.left.height - vertex.right.height == 2:
        # Нам нужны правые вращения.
        b = vertex.left
        C = b.right
        L = b.left

        if C.height <= L.height:
            # Нужно малое правое вращение.
            return small_right_rotation(vertex)
        else:
            # Нужно большое правое вращение.
            return big_right_rotation_short(vertex)