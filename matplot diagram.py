import matplotlib.pyplot as plt
import numpy as np

fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title("FRUITS")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()

