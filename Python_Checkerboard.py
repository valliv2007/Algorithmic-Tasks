"""You are trying to make a checkerboard made up of X's and O's. You've implemented the function before in a different language but it just won't work. The function creates an n by n board of X's and O's.

For example (Input --> Output)

n = 4 -->
[['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X'],
 ['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X']]"""


def make_checkered_board(n):
    result = []
    line_x = []
    line_o = []
    for i in range(n):
        if i % 2:
            line_x.append('O')
            line_o.append('X')
        else:
            line_x.append('X')
            line_o.append('O')
    for i in range(n):
        if i % 2:
            result.append(line_o)
        else:
            result.append(line_x)
    return result


print(make_checkered_board(5))


def bestmake_checkered_board(n):
    return [['O' if (i+j)%2!=0 else 'X' for i in range(n)] for j in range(n)]