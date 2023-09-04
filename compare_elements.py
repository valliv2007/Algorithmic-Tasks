digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...

cards = [2, 3, 7]
print(sorted(cards, key=lambda card: [-digit_lengths[card], card]))
