import cv2
from matplotlib import pyplot as plt
import numpy as np

I = cv2.imread('sarajevo.jpg')[:, :, ::-1]
I_ = np.swapaxes(I, 0, 1)
print(I_.shape)
print(I_)
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_)
plt.show()