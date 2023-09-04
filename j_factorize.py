def fz(n):
    ns = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ns.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ns.append(n)
    return ns

print(" ".join(map(str, fz(int(input())))))