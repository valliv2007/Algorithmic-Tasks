"""Task
An employee wishes to resign. Do not let him go.

Locate the entrance to his office so we can send its coordinates to the orbital obstacle placement service (OOPS).

The floor plan of the office is given as a list (python) or an array (java) of strings. Walls are marked 
with a # and interior with .. Strings can vary in length, and if they do, align them to the left.

Return the coordinates of the office entrance as a tuple (x, y) in python or Point in java. Top left is (0, 0), 
x is oriented to the right ("columns") and y downwards ("rows"):

+----> x
|
|
V
y
Examples
###.###
#.....#
#.....#  ->  (3, 0)
#....##
######

 #####
 #...#
 ....#
 #...#  ->  (1, 2)
##...#
#....#
######"""

from pprint import pprint
from typing import List, Tuple


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    for i, elem in enumerate(office):
        for j in range(len(elem)):
            if elem[j] == '.':
                if (not i or i == len(office) - 1 or not j or j == len(elem) - 1 or elem[j - 1] == ' ' or elem[j + 1] == ' '
                    or len(office[i - 1]) <= j or len(office[i + 1]) <= j or office[i - 1][j] == ' ' or office[i + 1][j] == ' '):
                    return j, i


print(locate_entrance(['#################', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '###.##.........##', '     #.........# ', '     #.........# ', '     #.........# ', '     ##........# ', '      #........# ', '      #........# ', '      #........# ', '      #........# ', '      ########## ']))
pprint(['#################', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '#...............#', '###.##.........##', '     #.........# ', '     #.........# ', '     #.........# ', '     ##........# ', '      #........# ', '      #........# ', '      #........# ', '      #........# ', '      ########## '])