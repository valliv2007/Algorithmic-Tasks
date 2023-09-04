"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""


from collections import defaultdict


def find_it(seq):
    amounts = defaultdict(int)
    for elem in seq:
        if amounts.get(elem):
            amounts.pop(elem)
        else:
            amounts[elem] += 1
    return list(amounts)[0]


from collections import Counter


def find_it_counter(seq):
    amounts = Counter(seq)
    for elem in list(amounts):
        if amounts[elem] % 2:
            return elem



print(find_it_counter([1,2,2,3,3,3,4,3,3,3,2,2,1]))