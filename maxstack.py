class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else print('error')

    def get_max(self):
        return print(max(self.items) if self.items else None)


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
