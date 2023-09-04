import array

a = int(input())
module = int(input())
s = [ord(i) for i in input()]
powers = array.array('I', [1])
sums = [(0, 0)]
hash_sum = 0
for index, char in enumerate(s):
    hash_sum = (sums[index][1] * a + char) % module
    sums.append((char % module, hash_sum))
    powers.append((powers[index] * a) % module)
amount = int(input())
for _ in range(amount):
    left, right = input().split()
    left = int(left)
    right = int(right)
    if left == right:
        print(sums[left][0])
    elif left == 1:
        print(sums[right][1])
    else:
        print((((sums[right - 1][1] * a + sums[right][0])
                - (sums[left - 2][1] * a + sums[left - 1][0])
                * powers[right - left + 1]) % module))
print(sums)
