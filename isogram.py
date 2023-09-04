def is_isogram(string):
    for index, char in enumerate(string.lower()):
        for sym in string.lower()[index + 1:]:
            if char == sym:
                return False
    return True

print(is_isogram('isogram'))