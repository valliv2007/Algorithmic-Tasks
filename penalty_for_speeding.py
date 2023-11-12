"""You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games. 
Before issuing penalty charge notice he gives you a choice to change your penalty.

Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of 
the police car chasing you, the number of police cars involved, etc. So, your task is to combine the given numbers and make 
the penalty charge to be as small as possible.

For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550

Examples:

['45', '30', '50', '1'] => '1304550'

['100', '10', '1'] => '100101'

['32', '3'] => '323'"""

from itertools import permutations


def smallnumberspenalty(numbers):
    return str(min([int(''.join(elem)) for elem in permutations(numbers)]))


def check(first, second):
    if first == second:
        return False
    for i in range(min(len(second), len(first))):
        if first[i] != second[i]:
            return first[i] < second[i]
    return check(first[len(second):], second) if len(first) >= len(second) else check(first, second[len(first):])


def penalty(numbers):
    numbers.sort()
    count = 0
    indexes =[]
    for i in range(1, len(numbers)):
        if numbers[i][0] == numbers[i - 1][0]:
            count += 1
            indexes.append(i)
    while count:
        for i in range(min(indexes), max(indexes) + 1):
            if check(numbers[i], numbers[i -1]):
                numbers[i], numbers[i -1] = numbers[i -1], numbers[i]
        count -= 1
    return ''.join(numbers)


def bestpenalty(numbers):
    return ''.join(sorted(numbers, key=lambda x: x*len(numbers)*10))


print(bestpenalty(['1234', '12341', '123412']))
print(penalty(['1234', '12341', '123412']))