"""Given two words, how many letters do you have to remove from them to make them anagrams?
Example
First word : c od e w ar s (4 letters removed)
Second word : ha c k er r a nk (6 letters removed)
Result : 10
Hints
A word is an anagram of another word if they have the same letters (usually in a different order).
Do not worry about case. All inputs will be lowercase."""

from collections import defaultdict


def anagram_difference(w1, w2):
    first = defaultdict(int)
    second = defaultdict(int)
    for char in w1:
        first[char] += 1
    for char in w2:
        second[char] += 1
    
    long, short = len(first), len(second)
    if short > long:
        first, second = second, first
    
    equals = 0

    for char in first:
        if first[char] == second.get(char):
            equals += first[char]
        elif second.get(char):
            equals += min(first[char], second.get(char))

    return len(w1) + len(w2) - equals * 2


from collections import Counter


def anagram_difference_best(w1, w2):
    c1, c2 = Counter(w1), Counter(w2)
    return sum(((c1 - c2) + (c2 - c1)).values())


print(anagram_difference('codewars', 'hackerrank'))