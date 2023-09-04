import cv2
import matplotlib.pyplot as plt


# Считывание изображения, которое должно быть преобразовано 
# в цветовое пространство HSV
image1 = cv2.imread('test.png')

# Преобразование изображения в цветовое пространство HSV 
# с помощью функции cvtColor и сохранение полученного изображения
imageresult = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
imageresult2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Вывод результата 
cv2.imshow("Start image", image1)
cv2.imshow("1", imageresult)
cv2.imshow("2", imageresult2)
cv2.waitKey(0)
img = cv2.imread('test.png')
edges = cv2.Canny(img,25,255,L2gradient=False)
cv2.imshow('Start image', img)
plt.imshow(edges, cmap='gray')
plt.show()
cv2.waitKey(0)