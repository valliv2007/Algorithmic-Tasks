def isLeapYear(year):
    
    return year % 400 == 0 or (year % 4 == 0 and  year % 100 != 0)

print(isLeapYear(1984))