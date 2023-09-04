class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if len(self.items) == 0:
            return 'error'
        else:
            self.items.pop()
    
    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        else:
            return max(self.items)
s = Stack()
n = int(input())
result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(int(command[1]))
    if command[0] == 'pop':
        if s.pop() == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(s.get_max())
    print(s.items)
for i in result:
    print(i)