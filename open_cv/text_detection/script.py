import cv2
from cv2 import COLOR_BGR2GRAY
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('text.png')

gray = cv2.cvtColor(img,COLOR_BGR2GRAY)

gray,img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2,1),np.uint8)

img = cv2.erode(gray,kernel,iterations=1)

img = cv2.dilate(img,kernel,iterations=1)

out_below = pytesseract.image_to_string(img)

cv2.imshow('Image',img)

print('OUTPUT: ',out_below)

cv2.waitKey(0)
cv2.destroyAllWindows()