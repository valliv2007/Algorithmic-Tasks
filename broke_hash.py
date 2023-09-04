import random
import string


def generate_str(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


a = 1000
module = 123987123
hash_sum_first = []
first_str = []
for i in range(26**20):
    s = generate_str(20)
    print(s)
    hash_sum = ord(s[0]) % module
    for char in s[1:]:
        hash_sum = (hash_sum * a + ord(char)) % module
    if hash_sum in hash_sum_first:
        print(hash_sum)
        print(s)
        index = hash_sum_first.index(hash_sum)
        print(first_str[index])
        break
    else:
        hash_sum_first.append(hash_sum)
        first_str.append(s) 

### 13971027
### fexlkmcaqcyfhkylzlbl
## ucusvsmcqakmimtfbopz