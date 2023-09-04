def fibbonachi(n):
    if n <= 1:
        return n
    return fibbonachi(n-2) + fibbonachi(n-1)


def fibbonachi_list(n):
    return [fibbonachi(i) for i in range(n+1)]


print(fibbonachi_list(int(input())))
