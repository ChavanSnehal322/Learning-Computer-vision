
#  Gradients and edge detection in images

import cv2 as cv
import numpy as np

 
img = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow('Banner', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray img', gray)

#  1] Laplacion edge detction
lap = cv.Laplacian(gray, cv.CV_64F )
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacion img', lap)                     # highlights the edges of the image ( pencil smugged sketch)



# 2] Sobel gradient 
#  detects the gradient in both x and y direction

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)      # gradients on x axis
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)        # gradients on y axis

comb_sobel = cv.bitwise_and(sobelx, sobely)

cv.imshow('Sobel X', sobelx)                                # displays gradients across y axis
cv.imshow('Sobel y img ', sobely)                           # displays gradients across x axis
cv.imshow('Combined sobel egdes ', comb_sobel)              # combined sobel image of x and y axis gradients


# Canny uses sobel in one of the stages to compute the image edges
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny img', canny)

#  Comparing Laplacion with Canny displays a poper sketch of the image edeges
# Sobel is mostly in advanced applications

cv.waitKey(0)