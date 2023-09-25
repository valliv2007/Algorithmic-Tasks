"""Let's define increasing numbers as the numbers whose digits, read from left to right, are never less than 
the previous ones: 234559 is an example of increasing number.

Conversely, decreasing numbers have all the digits read from left to right so that no digits is bigger than 
the previous one: 97732 is an example of decreasing number.

You do not need to be the next Gauss to figure that all numbers with 1 or 2 digits are either increasing or 
decreasing: 00, 01, 02, ..., 98, 99 are all belonging to one of this categories (if not both, like 22 or 55): 
101 is indeed the first number which does NOT fall into either of the categories. 
Same goes for all the numbers up to 109, while 110 is again a decreasing number.

Now your task is rather easy to declare (a bit less to perform): you have to build a function to return the 
total occurrences of all the increasing or decreasing numbers below 10 raised to the xth power (x will always be >= 0).

To give you a starting point, there are a grand total of increasing and decreasing numbers as shown in the table:

Total	Below
1	     1
10	     10
100	     100
475	     1000
1675	10000
4954	100000
12952	1000000
This means that your function will have to behave like this:

total_inc_dec(0)==1
total_inc_dec(1)==10
total_inc_dec(2)==100
total_inc_dec(3)==475
total_inc_dec(4)==1675
total_inc_dec(5)==4954
total_inc_dec(6)==12952
Tips: efficiency and trying to figure out how it works are essential: with a brute force approach, 
some tests with larger numbers may take more than the total computing power currently on Earth to be finished 
n the short allotted time.

To make it even clearer, the increasing or decreasing numbers between in the range 101-200 are: 
[110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 122, 123, 124, 125, 126, 127, 128, 129, 133, 134, 135, 136, 137, 138, 139, 
144, 145, 146, 147, 148, 149, 155, 156, 157, 158, 159, 166, 167, 168, 169, 177, 178, 179, 188, 189, 199, 200], 
that is 47 of them. In the following range, 201-300, there are 41 of them and so on, getting rarer and rarer.

Trivia: just for the sake of your own curiosity, a number which is neither decreasing of increasing is called 
a bouncy number, like, say, 3848 or 37294; also, usually 0 is not considered being increasing, decreasing or bouncy, 
but it will be for the purpose of this kata"""


def total_inc_dec(x):
    ten = 10 ** x
    century = 100
    if x == 0:
        return 1
    elif x == 1:
        return 10
    elif x == 2:
        return 100
    count = century + 1
    i = 110
    num = 0
    while i < ten:
        num += 1
        direction = None
        # print(i)
        step = 0
        for j in range(1, len(str(i))):
            if (direction == 'more' and str(i)[j] < str(i)[j - 1]) or (direction == 'less' and str(i)[j] > str(i)[j - 1]):
                if str(i)[j] < str(i)[j - 1]:
                    step = (int(str(i)[j - 1]) - int(str(i)[j])) * 10**(len(str(i)) - 1 -j)
                if str(i)[j] > str(i)[j - 1]:
                    step = (10 - int(str(i)[j])) * 10**(len(str(i)) - 1 -j)
                break
            else:
                if str(i)[j] < str(i)[j - 1]:
                    direction = 'less'
                elif str(i)[j] > str(i)[j - 1]:
                    direction = 'more'
                if j == len(str(i)) - 1:
                    if str(i)[j] < str(i)[j - 1]:
                        step +=  int(str(i)[j - 1]) - int(str(i)[j])
                    elif str(i)[j] > str(i)[j - 1]:
                        step = 10 - int(str(i)[j])
                    else:
                        step = 1
                    count += step
        i += step
    print(num)
    return count


print(total_inc_dec(10))