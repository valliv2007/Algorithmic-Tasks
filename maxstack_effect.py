class Stack:
    def __init__(self):
        self.items = []
        self.maximum = []

    def push(self, item):
        self.items.append(item)
        if not self.maximum or item >= self.maximum[-1]:
            self.maximum.append(item)

    def pop(self):
        if self.items and self.maximum:
            if self.items[-1] == self.maximum[-1]:
                self.maximum.pop()
        return self.items.pop() if self.items else print('error')

    def get_max(self):
        return print(self.maximum[-1] if self.maximum else None)


stack = Stack()
n = int(input())
for i in range(n):
    func = input().strip().split()
    if func[0][:3] == 'pop':
        stack.pop()
    elif func[0][:3] == 'get':
        stack.get_max()
    else:
        stack.push(int(func[1]))
