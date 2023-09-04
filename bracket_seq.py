def is_correct_bracket_seq(seq):
    if not seq:
        return print(True)
    brackets = {')': '(', ']': '[', '}': '{'}
    if len(seq) % 2 == 1 or seq[-1] not in brackets:
        return print(False)
    reverse_seq = seq[::-1]
    reverse_brackets = []
    is_correct = True
    for bracket in reverse_seq:
        if bracket in brackets:
            reverse_brackets.append(bracket)
        else:
            if bracket == brackets[reverse_brackets[-1]]:
                reverse_brackets.pop()
            else:
                is_correct = False
                break
    return print(is_correct)


is_correct_bracket_seq(list(input()))
