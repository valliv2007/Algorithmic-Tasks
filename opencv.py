# Импорт
import numpy as np
import cv2

# Позвоните в камеру компьютера, 0: первая основная камера
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Преобразование цветового пространства
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Отображение изображения
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)
    
    # Конец, клавиша q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закройте вызывающую программу камеры и закройте все окна изображений
cap.release()
cv2.destroyAllWindows()
