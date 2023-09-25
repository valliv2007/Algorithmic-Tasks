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
