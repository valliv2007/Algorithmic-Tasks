def gen_brackets(open_n, close_n, prefix, control):
    if open_n == 0 and close_n == 0:
        print(prefix)
    else:
        if open_n > 0:
            gen_brackets(open_n - 1, close_n, prefix + '(', control + 1,)
        if control > 0 and close_n > 0:
            gen_brackets(open_n, close_n - 1, prefix + ')', control - 1,)


open_n = close_n = int(input())
gen_brackets(open_n, close_n, "", control=0)
