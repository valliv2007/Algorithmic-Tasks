n, k = input().split()
prices = [int(i)for i in input().split()]
count = 0
prices.sort()
summ = 0
if int(k) >= prices[0]:
    for price in prices:
        summ += price
        if summ <= int(k):
            count += 1
        else:
            break
        
print(count)
