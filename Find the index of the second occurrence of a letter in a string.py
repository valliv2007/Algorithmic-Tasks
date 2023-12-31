"""In this kata, you need to write a function that takes a string and a letter as input and then returns 
the index of the second occurrence of that letter in the string. If there is no such letter in the string, 
then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.

Examples:

second_symbol('Hello world!!!','l') --> 3
second_symbol('Hello world!!!', 'A') --> -1
"""


def second_symbol(s, symbol):
    count = 0
    result = -1
    for i, letter in enumerate(s):
        if letter == symbol:
            count +=1
            if count >=2:
                return i
    return result

def second_symbol_cool(s, c):
    return s.find(c, s.find(c)+1)

