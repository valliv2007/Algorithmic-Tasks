class ListQueue:
    def __init__(self):
        self.items = []
        self.queue_size = 0
        self.head = 0

    def put(self, item):
        self.items.append(item)
        self.queue_size += 1

    def size(self):
        print(self.queue_size)

    def get(self):
        if self.queue_size == 0:
            return print('error')
        x = self.items[self.head]
        self.items[self.head] = None
        self.head += 1
        self.queue_size -= 1
        print(x)


n = int(input())
queue = ListQueue()
for i in range(n):
    full_command = input()
    command, *args = full_command.split()
    getattr(queue, command)(*args)
