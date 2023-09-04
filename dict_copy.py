a = {'1': 1, '2': 2, '3': 3}
b = a
s = a.copy()
print(a, b, s)

a['1'] = 0
print(a, b, s)

a['4'] = 4
print(a, b, s)

b['5'] = 5
print(a, b, s)

del a['4']
print(a, b, s)

del b['5']
print(a, b, s)

a.clear()
print(a, b, s)

a = {'6': 6, '7': 7, '8': 8}
print(a, b, s)

del a
print(b, s)

print("-------------------------copy------------------------")
import copy

c = {'1': 1, '2': 2, '3': [1, 2]}
d = copy.copy(c)
print(c, d)

c['1'] = 0
print(c, d)

c['3'].append(3)
print(c, d)

c['4'] = 4
print(c, d)

d['5'] = 5
print(c, d)

del c['4']
print(c, d)

del d['5']
print(c, d)

c = {'6': 6, '7': 7, '8': 8}
print(c, d)

del c
print(d)

print("-------------------------deepcopy------------------------")
x = {'1': 1, '2': 2, '3': [1, 2]}
y = copy.deepcopy(x)
print(x, y)

x['3'][-1] = 0
print(x, y)

x['3'].append(9)
print(x, y)