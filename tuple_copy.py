a = (1, 2, [1, 2])
b = a
print(a, b)

a[-1][-1] = 0
print(a, b)

b[-1].append(3)
print(a, b)

a = (6, 7, 8)
print(a, b)

del a
print(b)
print("-------------------------copy------------------------")

import copy

c = (1, 2, [1, 2])
d = copy.copy(c)
print(c, d)

c[-1][-1] = 0
print(c, d)

c[-1].append(3)
print(c, d)

print("-------------------------deepcopy------------------------")
x = (1, 2, [1, 2])
y = copy.deepcopy(x)

print(x, y)

x[-1][-1] = 0
print(x, y)

x[-1].append(9)
print(x, y)