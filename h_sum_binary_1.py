def get_sum(first, second):
    if  not second:
        return first
    sum_binary = ''
    add_one = False
    if len(second) > len(first):
        lng = second[::-1]
        short = first[::-1]
    else:
        lng = first[::-1]
        short = second[::-1]
    for i in range(len(lng)):
        try:
            sum_digits = int(lng[i]) + int(short[i]) + add_one
        except IndexError:
            sum_digits = int(lng[i]) + add_one
        if sum_digits == 2:
            sum_binary += '0'
            add_one = True
        elif sum_digits == 3:
            sum_binary += '1'
            add_one = True
        else:
            sum_binary += str(sum_digits)
            add_one = False
    if add_one:
        sum_binary += str(int(add_one))
    return sum_binary[::-1]

def read_input():
    first = input().strip()
    second = input().strip()
    return first, second

first, second = read_input()
print(get_sum(first, second))