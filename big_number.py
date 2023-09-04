n = int(input())
numbers = input().strip().split()


def is_number_bigger(number1, number2):
    if number1 == number2:
        return False
    if number1 == '1000':
        return True
    if number2 == '1000':
        return False
    if int(number1[0]) != int(number2[0]):
        return int(number1[0]) < int(number2[0])
    if len(number1) > 1 and len(number2) > 1:
        if int(number1[1]) != int(number2[1]):
            return int(number1[1]) < int(number2[1])
    elif len(number1) == 1:
        if number1[0] < number2[1]:
            return True
        elif number1[0] == number2[1] and len(number2) == 3:
            return number1[0] < number2[2]
        else:
            return False
    elif len(number2) == 1:
        if number2[0] < number1[1]:
            return False
        elif number2[0] == number1[1] and len(number1) == 3:
            return number2[0] > number1[2]
        else:
            return True
    if len(number1) > 2 and len(number2) > 2:
        return int(number1[2]) < int(number2[2])
    elif len(number1) == 2:
        if number1[0] < number2[2]:
            return True
        elif number1[0] == number2[2]:
            return number1[1] < number2[2]
        else:
            return False
    elif len(number2) == 2:
        if number2[0] < number1[2]:
            return False
        elif number2[0] == number1[2]:
            return number2[1] > number1[2]
        else:
            return True


def sort(numbers, n):
    for i in range(1, n):
        item = numbers[i]
        j = i
        while j > 0 and is_number_bigger(item, numbers[j - 1]):
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = item
    numbers.reverse()
    big_number = ''
    for number in numbers:
        big_number += number
    return big_number


print(sort(numbers, n))
