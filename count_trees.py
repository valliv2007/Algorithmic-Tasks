def count_trees(n):
    if n <= 1:
        return 1
    return (n - 2) * count_trees(n-2) + 2 * count_trees(n-1)


print(count_trees(int(input())))
