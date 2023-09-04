#  71639524

class EmptyDeque(Exception):
    """Дэк пуст"""


class FullDeque(Exception):
    """Дэк заполнен"""


class Deque:
    """Дэк"""
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__queue_size = 0

    def is_empty(self):
        return self.__queue_size == 0

    def previous(self, index, is_plus=False):
        idx = index + 1 if is_plus else index - 1
        return idx % self.__max_size

    def push_back(self, number):
        if self.__queue_size != self.__max_size:
            self.__queue[self.__tail] = number
            self.__tail = self.previous(self.__tail, True)
            self.__queue_size += 1
        else:
            raise FullDeque('error')

    def push_front(self, number):
        if self.__queue_size != self.__max_size:
            self.__queue[self.previous(self.__head)] = number
            self.__head = self.previous(self.__head)
            self.__queue_size += 1
        else:
            raise FullDeque('error')

    def pop_front(self):
        if self.is_empty():
            raise EmptyDeque('error')
        number = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.previous(self.__head, True)
        self.__queue_size -= 1
        return number

    def pop_back(self):
        if self.is_empty():
            raise EmptyDeque('error')
        number = self.__queue[self.previous(self.__tail)]
        self.__queue[self.previous(self.__tail)] = None
        self.__tail = self.previous(self.__tail)
        self.__queue_size -= 1
        return number


def main():
    amount = int(input())
    queue = Deque(int(input()))
    result = []
    for _ in range(amount):
        full_command = input()
        command, *args = full_command.split()
        try:
            result.append(getattr(queue, command)(*args))
        except (EmptyDeque, FullDeque):
            result.append('error')
    for value in result:
        if value:
            print(value)


if __name__ == '__main__':
    main()
