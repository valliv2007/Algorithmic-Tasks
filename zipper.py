from typing import List, Tuple

a = [1, 2, 3]
b = [4, 5, 6]
def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    x = []
    for index in range(0, len(a)):
        x.append(a[index])
        x.append(b[index])
    return x    

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
