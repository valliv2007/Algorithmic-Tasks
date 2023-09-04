"""Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work."""


def sum_strings(x, y):
    if not x and not y:
        return '0'
    if len(y) > len(x):
        x, y = y, x
    if not y:
        return x
    differense_length = len(x) - len(y)
    first_number_reverse = x[::-1]
    second_number_reverse = y[::-1]
    add = 0
    result = ''
    for i in range(len(second_number_reverse)):
        summ = int(first_number_reverse[i]) + int(second_number_reverse[i])
        result += str(summ + add)[-1]
        if len(str(summ + add)) > 1:
            add = int(str(summ + add)[0])
        else:
            add = 0
    result = result[::-1]
    if differense_length:
        begining = x[:differense_length]
        if add:
            first_part = ''
            end = 0
            for i in range(len(begining)):
                first_part += str(int(begining[-i - 1]) + add)[-1]
                if len(str(int(begining[-i - 1]) + add)) > 1:
                    add = int(str(int(begining[-i - 1]) + add)[0])
                else:
                    add = 0
                    end = -i -1
            if end:
                begining = begining[:end] + first_part[::-1]
                result = begining + result
            else:
                result = first_part[::-1] + result
        else:
            result = begining + result
    if add:
        result = '1' + result
    elif not int(result[0]):
        while not int(result[0]) and len(result) > 1:
            result = result[1:]
    return result


def bestsum_strings(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l-1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"


from gmpy2 import mpz

def cheatSsum_strings(x, y):
    return str(mpz(x or '0') + mpz(y or '0'))



print(sum_strings("99", '1'))