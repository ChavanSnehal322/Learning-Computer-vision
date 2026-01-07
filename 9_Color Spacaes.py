# Advanced
# Color Spaces - switching to different image space
# system to representing the pixel colors in array ( RDG, gray, HSV, LAV)

import cv2 as cv
import matplotlib.pyplot as plt


img  = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow("Banner", img)

plt.imshow(img)
plt.show( )           # prints image in RGB format 

#  BGR to gray scale
#  gray scale = pixel intensity of specific points in the img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale ', gray)

#  BGR to HSV ( Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV img', hsv)

#  BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB img', lab)

#  BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB img", rgb)

#  HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

#  LAB to BGR
lab_bgr = cv.cvtColor(img, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', lab_bgr)


#  gray to LAB not possible do gray to BGR and BGR to LAB

cv.waitKey(0)