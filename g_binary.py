def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    binary = ''
    if number == 0:
        return '0'
    result = number
    while result !=0:
        binary_digit = result % 2
        binary = binary + str(binary_digit)
        result = int((result - binary_digit) / 2)    
    return binary[::-1]
    
def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))