"""Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""

def highest_rank(arr):
    arr.sort()
    counter = {arr.count(elem): elem for elem in arr}
    return counter[max(counter)]


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))

def besthighest_rank(arr):
    return max(sorted(arr, reverse=True), key=arr.count)

print(besthighest_rank([1, 10, 10, 1, 7, 6, 4, 11, 1]))