''' Photo Scketching '''

from calendar import c
import cv2
from matplotlib.pyplot import sca

img = cv2.imread('mon.jpg')

## image to gray filter
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# inverted gray image
inv_gray_img = 255 - gray_img

# bluring 

blured_img = cv2.GaussianBlur(inv_gray_img,(19,19),0)

# inverted blured image
inv_blured_img = 255 - blured_img

# preparing photo 
sketch = cv2.divide(gray_img,inv_blured_img,scale=256.0)

cv2.imshow('Orginal Image',img)

cv2.imshow('Pencil Sketch',sketch)

cv2.waitKey(0)