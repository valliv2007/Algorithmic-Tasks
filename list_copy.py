a = [1, 2, 3]
b = a
s = a.copy()
print(a, b, s)
print(b is a, s is a)

a[0] = 0
print(a, b, s)

a.append(4)
print(a, b, s)

b.append(5)
print(a, b, s)

a.pop()
print(a, b, s)

b.pop(1)
print(a, b, s)

s.append(8)
print(a, b, s)

a.reverse()
print(a, b, s)

a.clear()
print(a, b, s)

a = [6, 7, 8]
print(a, b, s)

del a
print(b, s)
print("-------------------------copy------------------------")
import copy

c = [1, 2, [1, 2]]
d = copy.copy(c)
k = c.copy()
print(c, d, k)
print(c is d, c[-1] is d[-1])

c[0] = 0
print(c, d, k)

c[-1].append(3)
print(c, d, k)

c.append(4)
print(c, d, k)

d.append(5)
print(c, d, k)

c.pop()
print(c, d, k)

d.pop(1)
print(c, d, k)

c.reverse()
print(c, d, k)

c.clear()
print(c, d, k)

c = [6, 7, 8]
print(c, d, k)

del c
print(d, k)

print("-------------------------deepcopy------------------------")
x = [1, 2, [1, 2]]
y = copy.deepcopy(x)
print( x[-1] is y[-1])

print(x, y)

x[-1][-1] = 0
print(x, y)

x[-1].append(9)
print(x, y)