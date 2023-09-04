#  71606998

import operator


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()


def get_result(seq):
    stack = Stack()
    operators = {'+': operator.add,
                 '*': operator.mul,
                 '-': operator.sub,
                 '/': operator.floordiv}
    for symbol in seq:
        if symbol in operators:
            last_number = stack.pop()
            result = operators[symbol](stack.pop(), last_number)
        else:
            result = symbol
        stack.push(int(result))

    return stack.pop()


if __name__ == '__main__':
    print(get_result(input().strip().split()))
