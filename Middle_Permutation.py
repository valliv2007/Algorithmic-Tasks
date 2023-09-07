"""Task
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation."""
from itertools import permutations
from math import factorial

def oldmiddle_permutation(string):
    variants = list(permutations(string))
    variants.sort()
    if len(variants) % 2:
        result = variants[int(len(variants)/2)]
    else:
        result = variants[int(len(variants)/2) - 1]
    return ''.join(map(str, result))


def middle_permutation(string):
    string_list = sorted(string)
    result = ''
    index_main = factorial(len(string_list)) // 2 - 1
    while string_list:
        amount = factorial(len(string_list) - 1)
        index_remove = index_main // amount
        index_main = index_main % amount
        result += string_list[index_remove]
        string_list.pop(index_remove)
    return result


def bestmiddle_permutation(string):
    s = sorted(string)
    if len(s) % 2 == 0:        
        return s.pop(len(s)//2-1) +''.join(s[::-1])
    else:
        return s.pop(len(s)//2) + bestmiddle_permutation(s)


print(middle_permutation("0123456789"))