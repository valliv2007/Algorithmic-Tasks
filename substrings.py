s = input()
chars = []
count = 0
max_count = 0
start = 0
for char in s:
    if char not in chars[start:]:
        chars.append(char)
        count += 1
    else:
        if count > max_count:
            max_count = count
        new_start = chars.index(char) + 1
        chars.append(char)
        count -= new_start - start
        start = new_start
if count > max_count:
    max_count = count      
print(max_count)