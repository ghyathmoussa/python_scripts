''' Edge Detection Script '''

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('car.jpg')

edges = cv2.Canny(img,100,100)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Orginal Image'),plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edges,cmap='gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()