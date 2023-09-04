numbers = [1,2,3,4,5]
squared_numbers = (number**2 for number in numbers)
print(type(squared_numbers))
print(list(squared_numbers))
print(list(squared_numbers))

set_of_numbers = {1,2,3}
numbers_iterator = iter(set_of_numbers)
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))