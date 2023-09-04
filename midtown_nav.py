"""Create a function that tells the user how to get around Midtown in Manhattan. The function should be able to help 
the user to get from one location in this area to another.

Streets run east-west. Street numbers increase as they move northward, from 1st street in Greenwich Village 
to 220th street in the Inwood section. Avenues run south-north, with numbers beginning on the east side 
of the island and increase to the west.

"The Encyclopedia of New York City" defines Midtown as extending from 34th Street to 59th Street (going northwards) 
and from 3rd Avenue to 8th Avenue (going westwards).

Streets are prefixed with E or W depending on if the adress is on the eastside or westside (East or West of 5th Avenue).

For example:

start = "8th Ave and W 38th St"
end = "7th Ave and W 36th St"
The code above should tell the user how to get from 8th Ave and W 38th St to 7th Ave and W 36th St. It should 
then output as a string how many blocks north/south, and then how many blocks east/west the user should travel.

start = "8th Ave and W 38th St"
end = "7th Ave and W 36th St"
output => "Walk 2 blocks south, and 1 blocks east"

start = "5th Ave and E 46th St"
end = "7th Ave and W 58th St"
output => "Walk 12 blocks north, and 2 blocks west"
Note: When the avenues are same, the direction of movement should be west and when the streets are same 
the direction should be north."""

import re


def midtown_nav(start, end):
    start_ave = int(start[0])
    end_ave = int(end[0])
    start_st = int(re.split(r'[W,E] ', start)[-1][0:2])
    end_st = int(re.split(r'[W,E] ', end)[-1][0:2])
    ave_mov = end_ave - start_ave
    st_mov = end_st - start_st
    ave_dir = ('west' if ave_mov >= 0 else 'east')
    st_dir = ('north' if st_mov >= 0 else 'south')
    return f'Walk {abs(st_mov)} blocks {st_dir}, and {abs(ave_mov)} blocks {ave_dir}'

print(midtown_nav("5th Ave and E 46th St", "7th Ave and W 58th St"))