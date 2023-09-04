from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    chars = {}
    result = None
    for char in longer:
        try:
            chars[char] += 1
        except KeyError:
            chars[char] = 1
    for char in shorter:
        chars[char] += 1
    for char in chars:
        if chars[char] % 2 != 0:
            result = char
    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
