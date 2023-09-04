import numpy as np
a = np.array([1, 2, 3])
print(a)
print(type(a))
b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b)
print(type(b))
c = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex64)
print(c)
d = np.zeros((3, 5))
print(d)
e = np.ones((2,2,2))
print(e)
f = np.eye(5)
print(f)
g = np.empty((3,3))
print(g)
h = np.arange(10, 35, 5)
print(h)
i = np.linspace(1.5, 2.4, 10)
print(i)

def f1(i, j):
    return 4*i +j

k = np.fromfunction(f1, (3,3))
print(k)
np.set_printoptions(threshold=2999, precision=2)
print(np.arange(0, 3000, 1))
