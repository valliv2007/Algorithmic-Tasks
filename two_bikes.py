def get_day(numbers, price, left, right):
    if left >= right:
        return -1
    mid = (left + right) // 2
    if int(numbers[mid]) >= price and (int(numbers[mid - 1]) < price or mid == 0):
        return mid + 1
    elif int(numbers[mid]) < price:
        return get_day(numbers, price, mid + 1, right)
    else:
        return get_day(numbers, price, left, mid)


_ = int(input())
numbers = input().strip().split()
price = int(input())

print(f'{get_day(numbers, price, left=0, right=len(numbers))} {get_day(numbers, price * 2, left=0, right=len(numbers))}')
