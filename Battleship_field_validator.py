"""Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if 
it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. 
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid 
containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. 
The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. 
In this kata we will use Soviet/Russian version of the game.
Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). 
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner."""


from collections import defaultdict


def validate_battlefield(field):
    battleship = 0
    cruiser = 0
    destroyer = 0
    submarine = 0
    block_index_current = set()
    current_ship_y = defaultdict(int)
    for i in range(10):
        current_ship_x = 0
        block_index_next = set()
        for j in range(10):
            # print(j, current_ship_x)
            if field[i][j]:
                if j in block_index_current:
                    return False
                current_ship_x += 1
                if j < 9 and field[i][j+1]:
                    block_index_next.add(j)
                    block_index_next.add(j - 1)
                    block_index_next.add(j + 1)
                elif (i < 9 and field[i+1][j]) or current_ship_y.get(str(j)):
                    block_index_current.add(j+1) 
                    current_ship_x = 0 
                    current_ship_y[str(j)] += 1
                    if i == 9 or not field[i+1][j]:
                        if current_ship_y[str(j)] == 4:
                            battleship += 1
                        elif current_ship_y[str(j)] == 3:
                            cruiser += 1
                        elif current_ship_y[str(j)] == 2:
                            destroyer += 1
                        if battleship > 1 or cruiser > 2 or destroyer > 3:
                            return False
                        current_ship_y[str(j)] = 0
            else:
                if current_ship_x:
                    block_index_next.add(j)
                if current_ship_x == 4:
                    battleship += 1
                elif current_ship_x == 3:
                    cruiser += 1
                elif current_ship_x == 2:
                    destroyer += 1
                elif current_ship_x == 1:
                    submarine += 1
                    block_index_next.add(j - 1)
                    block_index_next.add(j - 2)
                if battleship > 1 or cruiser > 2 or destroyer > 3 or submarine > 4:
                    return False
                current_ship_x = 0
           #  print(i, j, current_ship_x, submarine)
        if current_ship_x == 4:
            battleship += 1
        elif current_ship_x == 3:
            cruiser += 1
        elif current_ship_x == 2:
            destroyer += 1
        elif current_ship_x == 1:
            submarine += 1
            block_index_next.add(j - 1)
            block_index_next.add(j)
        if battleship > 1 or cruiser > 2 or destroyer > 3 or submarine > 4:
            return False
        current_ship_x = 0
        block_index_current = block_index_next
    block_index_current = set()
    # print(battleship, cruiser, destroyer, submarine)
    if battleship != 1 or cruiser != 2 or destroyer != 3 or submarine != 4:
        return False
    return True


print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))