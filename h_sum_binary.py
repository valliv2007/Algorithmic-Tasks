def to_binary(number):
    binary = ''
    if number == 0:
        return '0'
    result = number
    while result !=0:
        binary_digit = result % 2
        binary = binary + str(binary_digit)
        result = int((result - binary_digit) / 2)    
    return binary[::-1]

def get_sum(first_number, second_number):
    first_number_reverse = first_number[::-1]
    second_number_reverse = second_number[::-1]
    first_number_dec = 0
    second_number_dec = 0
    for i in range(len(first_number_reverse)):
        first_number_dec += int(first_number_reverse[i]) * (2 ** i) 
    for i in range(len(second_number_reverse)):
        second_number_dec += int(second_number_reverse[i]) * (2 ** i) 
    return to_binary(first_number_dec + second_number_dec)

    
def read_input():
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))