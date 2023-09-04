class B:
    x = 5


a = B()
b = B()


a.x = 2

print(a.x, b.x, B.x)

B.x = 8

print(a.x, b.x, B.x)

del a.x

print(a.x, b.x, B.x)

del B.x

print(getattr(B, 'x', False), getattr(a, 'x', False))
B.prop = 'ff'
print(hasattr(B, 'prop'), hasattr(a, 'prop'))
a.prop = 'jjjj'

print(b.prop, a.prop)
del a.prop
print(b.prop, a.prop)