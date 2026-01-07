
#  Contour detection on image
#  finding the bounderies of images used in image object analysis

import cv2 as cv
import numpy as np


img  = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')

cv.imshow("banner", img)

#  blank image to draw contours on it 
blank = np.zeros(img.shape , dtype='uint8')
cv.imshow('Blank', blank)


#  converting to grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

#  blur - to reduce unvanted contour
blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


#  canny 
canny = cv.Canny(blur, 125, 170)
cv.imshow('Canny img', canny)

#  Threshold ( instead of blur and Canny)
#  converting the image to binary form
ret, thresh = cv.threshold(grey, 120, 250, cv.THRESH_BINARY)
cv.imshow('Thres img ', thresh)


#  return contours (list of all boundiers pixels in image) and hierarchy
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# RETR_list  = returns all contours in image
# RETR_TREE = returns hierarchical contours

print(f'{len(contours)} contours(s) found in the image')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Countors on blank', blank)    # almost same to canny image





cv.waitKey(0)