"""Create a function mispelled(word1, word2):

mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
mispelled('versed', 'versed') #returns True 
It checks if the word2 differs from word1 by at most one character.

This can include an extra char at the end or the beginning of either of words.

In the tests that expect true, the mispelled word will always differ mostly by one character. 
If the two words are the same, return True."""

def mispelled(word1,word2):
    if word2 == word1:
        return True
    if abs(len(word1) - len(word2)) > 1:
        return False
    if (len(word1) == 1 and len(word2) == 0) or (len(word1) == 0 and len(word2) == 1):
        return True
    if len(word1) > len(word2):
        if word1[:-1] == word2:
            return True
        elif word1[1:] == word2:
            return True
        else:
            return False
    if len(word2) > len(word1):
        if word2[:-1] == word1:
            return True
        elif word2[1:] == word1:
            return True
        else:
            return False
    mistakes = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            mistakes +=1
        if mistakes > 1:
            return False
    return True


def mispelled_short(word1, word2):
    if word1 == word2:
        return True
    if abs(len(word1) - len(word2)) > 1:
        return False
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    for i in range(len(word2)):
        if word1[i] != word2[i]:
            if len(word1) == len(word2):
                return word1[i+1:] == word2[i+1:]
            else:
                return word1[i+1:] == word2[i:]
    return True


print(mispelled("hhhgjg", "hagjg"))