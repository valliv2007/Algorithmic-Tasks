import cv2
import numpy as np
import matplotlib.pyplot as plt

my_picture = cv2.imread('sarajevo.jpg')[:, :, ::-1]
# cv2.imshow('Display', my_picture)
result_1 = cv2.resize(my_picture, None, fx=2, fy=2)
result_2 = cv2.resize(my_picture, None, fx=0.5, fy=0.5)
plt.imshow(result_1)
plt.show()
plt.imshow(result_2)
plt.show()