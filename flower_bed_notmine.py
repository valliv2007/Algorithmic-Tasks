def calculate(flowers):
    result = []
    result.append(flowers[0])
    for flower in flowers[1::]:
        append_box = True
        if result[-1][0] <= flower[0] <= result[-1][1] and flower[1] > result[-1][1]:
            result[-1][1] = flower[1]
            append_box = False
            pass
        elif flower[0] <= result[-1][0] or flower[1] <= result[-1][1]:
            append_box = False
            pass
        if append_box:
            result.append(flower)
    return result

def read_input():
    n = int(input())
    flower_beds = []
    for i in range(n):
        flower_beds.append(list(map(int, input().strip().split())))
    return flower_beds

def main():
    flowers = sorted(read_input())
    for flow in calculate(flowers):
        print(*flow)

if __name__ == '__main__':
    main()
