"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"""


def strip_comments(strng, markers):
    strings = strng.split('\n')
    new_strings = []
    for string in strings:
        i = len(string)
        for marker in markers:
            try:
                im = string.index(marker)
            except ValueError:
                continue
            if im < i:
                i = im
        new_string = string[:i].rstrip()
        new_strings.append(new_string)
    return '\n'.join(map(str, new_strings))


def bestsolution(string, markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))
