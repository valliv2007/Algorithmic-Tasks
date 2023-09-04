def merge_flower_beds(flower_beds):
    flower_beds.sort()
    result = [flower_beds[0]]
    for segment in flower_beds[1:]:
        is_add = True
        if result[-1][0] <= segment[0] <= result[-1][1] and segment[1] > result[-1][1]:
            result[-1][1] = segment[1]
            is_add = False
        elif segment[0] <= result[-1][0] or segment[1] <= result[-1][1]:
            is_add = False
        if is_add:
            result.append(segment)
    return result


def read_input():
    n = int(input())
    flower_beds = []
    for i in range(n):
        flower_beds.append(list(map(int, input().strip().split())))
    return flower_beds


for result in merge_flower_beds(read_input()):
    print(*result)