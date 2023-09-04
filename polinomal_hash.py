a = int(input())
module = int(input())
s = input()
power = len(s)
if power:
    hash_sum = ord(s[0]) % module
else:
    hash_sum = 0
if power > 1:
    for char in s[1:]:
        hash_sum = (hash_sum * a + ord(char)) % module

print(hash_sum)
