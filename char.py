def printer_error(s):
    # your code
    length = len(s)
    forbidden_letters = [chr(i) for i in range(110, 123)]
    count = 0
    for char in s:
        if char in forbidden_letters:
            count += 1
    return f'{count}/{length}'


def printer_error_1(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)


print('O' > 'M') 
