"""Tolkein's publisher wishes to implement an online store for the "Lord of the Rings" and "The Hobbit" books. 
Each book costs $10. However, if 2 titles are purchased, a 5% discount will be received, i.e. purchasing
 "Fellowship of the Ring" and "Two Towers" will cost $19. If 3 different titles are purchased, a 10% discount
  will be received. The purchase of all 4 different titles will receive a 20% discount. An additional single 
  title will be full-price.

The encoding of an order will be in the form of strings in an array. For example: [“F”, “T”, “R”, “H”, “H”] 
is the encoding of 2 copies of "The Hobbit" and a single copy of each of the titles in the "Lord of the Rings" trilogy.

The expected output is a number. E.g. 42 is the expected output for the example above. The output should be the 
cheapest total cost. For example - if the book order is ["F", "T", "H", "F", "T", "R"], valid total costs 
include (3*10 discounted by 10%) + (3*10 discounted by 10%) and (4*10 discounted by 20%) + (2*10 discounted by 5%). 
The cheapest total cost is 51
"""

def final_sum(values):
    price = 10
    discounts = {2: 0.95, 3: 0.9, 4: 0.8}
    if len(values) <= 1:
        return int(values[0] * price) if len(values) else 0
    if not values[0]:
        return 0
    summ = int(values[-1] * price * discounts.get(len(values), 0) *len(values))
    del_elem = values.pop()
    return summ + final_sum([elem - del_elem for elem in values])
    
def calculate_cart_total(contents):

    titles = {'F': 0, 'R': 0, 'T': 0,'H': 0,}

    for title in contents:
        titles[title] += 1
    values = [*titles.values()]
    values.sort()
    values.reverse()
    return final_sum(values)
    
def calculate_cart_total_wrong(contents):
    price = 10
    discounts = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8}
    sum_first = 0
    sum_reverse = 0
    books = set()

    for title in contents:
        if title not in books:
            books.add(title)
        else:
            sum_first += int(len(books) * price * discounts[len(books)])
            books = {title}

    sum_first += int(len(books) * price * discounts.get(len(books), 0))
    books.clear()

    for title in contents[::-1]:
        if title not in books:
            books.add(title)
        else:
            sum_reverse += int(len(books) * price * discounts[len(books)])
            books = {title}
    sum_reverse += int(len(books) * price * discounts.get(len(books), 0))

    return sum_first if sum_reverse > sum_first else sum_reverse


print(calculate_cart_total(["F", "T", "H", "F", "T", "R"]))