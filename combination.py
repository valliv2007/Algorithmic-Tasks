def combinate_letters(digits):
    if not digits:
        return []

    buttons = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

    def add_letter(combination, next_digit):
        if len(next_digit) == 0:
            result.append(combination)
        else:
            for letter in buttons[next_digit[0]]:
                add_letter(combination + letter, next_digit[1:])

    result = []
    add_letter('', digits)
    return result


print(*combinate_letters(input()), sep=' ')
