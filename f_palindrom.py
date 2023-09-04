def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    clean_line = ''.join(filter(str.isalnum, line.lower()))
    
    for index in  range(len(clean_line)):
        if clean_line[index] != clean_line[(-1) - index]:
            return False

    return True


print(is_palindrome(input().strip()))