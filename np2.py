import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
b1 = b
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a%b)
print(a/b)
print(a+1)
print(a*2)
print(a**3)
print(a < 44)
print(a < b)
b[1] = 31
print(a < b)
print(np.cos(a))
print(np.arctan(a))
c = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(c))
print(c.sum())
print(c.min())
print(c.max())
print(c.min(axis=0))
print(c.min(axis=1))

d = np.array([[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]])
print(d[2, 3])
print(d[(3, 1)])
print(d[0][2])
print(d[:, 2])
print(d[:2])
print(d[1:3, : :])
print(d[:,-1])
e = np.array(([[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]))
print(e)
print(e.shape)
print(e[1, ...])
print(e[ ..., 0])
for row in e:
    print(row)

for element in e.flat:
    print(element)

print(e.ravel())
e.shape = (3,4)
print(e)
print(e.transpose())
print(e.transpose().reshape(2, 6))
f = np.array([[  0,   1],
       [  2,  10],
       [ 12,  13],
       [100, 101],
       [102, 110],
       [112, 113]])
print(f)
print(f.reshape((12, 1), order='F'))
print(f)
f.resize(3, 4)
print(f)
print(f.reshape(2, -1))
g = np.array([[1, 2], [3, 4]])
h = np.array([[5, 6], [7, 8]])
print(np.vstack((g, h)))
print(np.hstack((g, h)))
print(np.column_stack((g, h)))
print(np.row_stack((g, h)))
i =  np.arange(12).reshape((2, 6))
print(i)
print(np.hsplit(i, 3))
print(np.hsplit(i, (1, 5)))
print(np.vsplit(i, 2))
j = np.arange(12)
k = j
l = j.view()
print(k is j)
print(l is j)
print (l.base is j)
k.shape = (3, 4)
print(j)
l.shape = (12, 1)
print(j)
l[0,0] = 999
print(j)
m = j[:, 1:3]
print(m)
m[:] = 10
print(j)
n = j.copy()
print(n is j, n.base is j)
n[-1, -1] = 999
print(j)
