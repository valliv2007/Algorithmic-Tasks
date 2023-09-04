import math
def is_power_of_four(number: int) -> bool:
   return  4**(int(math.log(number,4))) == number

print(is_power_of_four(int(input())))   