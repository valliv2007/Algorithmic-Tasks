"""You have a positive number n consisting of digits. You can do at most one operation: Choosing the index 
of a digit in the number, remove this digit at that index and insert it back to another or at the same place
 in the number in order to find the smallest number you can get.

Task:
Return an array or a tuple or a string depending on the language (see "Sample Tests") with

the smallest number you got
the index i of the digit d you took, i as small as possible
the index j (as small as possible) where you insert this digit d to have the smallest number.
Examples:
smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].
29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is 
the number 29917.
smallest(187863002809) --> [18786300289, 10, 0]
smallest(1000000) --> [1, 0, 6] or ...
Note
Have a look at "Sample Tests" to see the input and output in each language"""


def smallest(n):
    previous = [int(num) for num in str(n)]
    min_number = min(previous)
    min_count = previous.count(min_number)
    min_index = previous.index(min_number)
    insert_index = 1
    if min_index == 1 and (min_count == 1 or previous[2] < previous[0]):
        for index in range(2, len(previous)):
            if previous[index] > previous[0]:
                insert_index = index
                break
            if index == len(previous) - 1:
                insert_index = len(previous)
        while previous[insert_index - 1] == previous[0]:
            insert_index -= 1
        elem = previous.pop(0)
        previous.insert(insert_index - 1, elem)
        return [int(''.join(map(str, previous))), 0, insert_index - 1]
    if min_count > 1:
        new_min_index = len(previous) - previous[::-1].index(min_number) - 1
        if previous[new_min_index - 1] != min_number:
            min_index = new_min_index
        else:
            for i in range(2, new_min_index):
                if previous[new_min_index - i] != min_number:
                    min_index = new_min_index - i + 1
                    break
    if min_index > 1:
        elem = previous.pop(min_index)
        previous.insert(0, elem)
        return [int(''.join(map(str, previous))), min_index, 0]
    else:
        first_elem = min_number
        result = smallest(int(str(n)[1:]))
        return [int(str(first_elem) + str(result[0])), result[1] + 1, result[2] + 1]

def smalles_best(n):
	s = str(n)
	min1, from1, to1 = n, 0, 0
	for i in range(len(s)):
		removed = s[:i] + s[i+1:]
		for j in range(len(removed)+1):
			num = int(removed[:j] + s[i] + removed[j:])
			if (num < min1):
				min1, from1, to1 = num, i, j
	return [min1, from1, to1]


print(smallest(503424020178946429))
print(smallest(408985796550706399))
print(smallest(81927149614878434))
print(smallest(275764633635589748))
print(smallest(404556878696927412))
print(smallest(601455135067863520))
print(smallest(192993463954868867)) 



