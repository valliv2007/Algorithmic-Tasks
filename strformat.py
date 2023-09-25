x = 'Hello {a}{b}'
y = 'Hello {}{}'
z = 'Hello {0}{1}'
a = "price: {:.2f}"
b = "price: {:^7} dollars"
c = 'temp : {:=10} degrees'
d = 'temp : {:+} degrees'
e = 'temp : {: } degrees today, tomorrow {: } degrees'
f = 'my income {:,}'
g = 'my income {:_}'
h = '5 =  {:b}'
i = 'a =  {:c}'
j = '0b101 =  {:d}'
k = '1000 = {:e}'
l = '1.000000e+03 = {:g}'
m = '9 = {:o}'
n = '30 = {:X}'
o = '10 = {:n}'
p = '0.1 = {:.2%}'
print(x.format(a='World', b='!'))
print(y.format('World', '!'))
print(z.format('World', '!'))
print(a.format(45.5855858))
print(b.format(46))
print(c.format(-46))
print(d.format(46))
print(e.format(2,-1))
print(f.format(100000000))
print(g.format(100000000))
print(h.format(5))
print(i.format(97))
print(j.format(0b101))
print(k.format(1000))
print(l.format(1.000000e+03))
print(m.format(9))
print(n.format(30))
print(o.format(0xa))
print(p.format(0.1))