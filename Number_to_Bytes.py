"""In this kata, your task is to write a function to_bytes(n) (or toBytes(n) depending on language)
that produces a list of bytes that represent a given non-negative integer n. Each byte in the list is
represented by a string of '0' and '1' of length 8.
The most significant byte is first in the list"""

import textwrap


def to_bytes(n):
    binary = str(bin(int(n)))[2:]
    if len(binary) % 8:
        binary = binary.zfill((8 - (len(binary) % 8)) + len(binary))
    return textwrap.wrap(binary, 8)


print(to_bytes(65537))
