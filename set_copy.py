a = {1, 2, 3}
b = a
s = a.copy()
print(a, b, s)

a.add(4)
print(a, b, s)

b.add(5)
print(a, b, s)

a.pop()
print(a, b, s)

b.remove(5)
print(a, b, s)

a.clear()
print(a, b, s)


a = {6, 7, 8}
print(a, b, s)

del a
print(b, s)
print("-------------------------copy------------------------")
import copy

c = [1, 2, [1, 2]]
d = copy.copy(c)
print(c, d)

c[0] = 0
print(c, d)

c[-1].append(3)
print(c, d)

c.append(4)
print(c, d)

d.append(5)
print(c, d)

c.pop()
print(c, d)

d.pop(1)
print(c, d)

c = [6, 7, 8]
print(c, d)

del c
print(d)

print("-------------------------deepcopy------------------------")
x = [1, 2, [1, 2]]
y = copy.deepcopy(x)

print(x, y)

x[-1][-1] = 0
print(x, y)

x[-1].append(9)
print(x, y)