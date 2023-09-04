class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def push(self, x):
        if self.queue_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.queue_size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return print(None)
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.queue_size -= 1
        return print(x)

    def peek(self):
        print(None if self.is_empty() else self.queue[self.head])

    def size(self):
        print(self.queue_size)


amount = int(input())
queue = MyQueueSized(int(input()))
for i in range(amount):
    full_command = input()
    command, *args = full_command.split()
    getattr(queue, command)(*args)
