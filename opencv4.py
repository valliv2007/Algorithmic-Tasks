import cv2
import matplotlib.pyplot as plt
import numpy as np

img_1 = cv2.imread('test2.png')
img_2 = cv2.imread('test1.png')

# Создаём копию изначального изображения
img_cont = img_1.copy()

# Переводим изначальное изображение img в серый канал (с этим методом
# мы познакомились выше) и сохраняем в переменной gray
gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# Производим изменение размерности в 4 раза (изменение размерности производится
# в пикселях) относительно изначальной картинки img и сохраняем полученное 
# изображение в переменной img_resize
img_resize = cv2.resize(img_1, (int(img_1.shape[1] / 4), int(img_1.shape[0] / 4)))

# Далее идёт большой блок кода, в котором мы создаём 
# алгоритм детектирования краёв Canny Edge Detector (с этим методом
# мы познакомились выше) 
canny_1 = 200
canny_2 = 225
canny = cv2.Canny(img_1, canny_1, canny_2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
min_black = 255
cnt_black = []

for cnt in contours:
    c_area = cv2.contourArea(cnt) + 1e-7
    if cv2.contourArea(cnt) + 1e-7 > 500:
        cv2.drawContours(img_cont, [cnt], -1, 3)
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [cnt], -1, (255,255,255), -1)
        temp_mask = cv2.bitwise_and(gray, mask)
        temp_col = np.sum(temp_mask).real/(cv2.contourArea(cnt)+1e-7)
        if (temp_col < min_black) or (len(cnt_black) == 0):
            cnt_black = cnt
            min_black = temp_col

if len(cnt_black)!=0:
    cv2.drawContours(img_cont, [cnt_black], -1, (0,0,255), 3)

cv2.imshow('First image', img_1)
cv2.imshow('Second image', img_2)
# Вывод на экран изображения с детектированными контурами
cv2.imshow('Contour image', img_cont)
# Вывод на экран изображения в сером цветовом канале
cv2.imshow('Gray channel image', gray)
# Вывод на экран уменьшенного в 4 раза изображения 
cv2.imshow('Resize image', img_resize)

# Режим ожидания нажатия кнопки
cv2.waitKey(0)