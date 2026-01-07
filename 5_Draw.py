# drawing and writing on the images
# 
# 


import cv2 as cv

import numpy as np


# blank image creation( reading img)
blank = np.zeros((500, 500), dtype = 'uint8')

# opens a blank canvas window to draw
# cv.imshow('Blank canvas', blank)

# reading image
img = cv.imread('Reading a video Images/Photos/images.jpeg')

# cv.imshow('building', img)



###################################

# printing image color

#  blank img creation
blank1 = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# blank1[:] = 0,255,0         # painting whole grid green

# Displays a blank green grid window
# cv.imshow('Green', blank1)

# displays red grid of window
# blank1[:] = 0, 0, 255
# cv.imshow('Red', blank1)
#####################################################

# passing range of the pixels of image

blank3 = np.zeros((500, 500, 3), dtype = 'uint8')

blank3[200: 300, 400 : 500] = 255, 0, 0
# cv.imshow('Blue', blank3)


################################################

# Drawing a rectangle
# ( image name, rectangle points ( x and y co ordinates), color co ordinates(green), thikness)
cv.rectangle(blank1, (0, 0), (250, 250), (0, 250, 0), thickness = 2)

# cv.imshow( 'Rectangle', blank1)


# drawing square half the size of the grid
# thickness = -1 fill the shape with the border color
cv.rectangle( blank1, (0,0), (blank1.shape[1] // 2, blank1.shape[0] // 2), (0, 255, 0), thickness = -1)

# cv.imshow('Square', blank1)


# draw circle
# attributes : image name, center co ordinates, radius, color 
cv.circle(blank1, (blank1.shape[1] // 2, blank1.shape[0] // 2), 100, (0, 0, 255), thickness = -1)

# cv.imshow('Circle', blank1)

# standard line
cv.line(blank1, (0,0), (blank1.shape[1] // 2, blank1.shape[0] // 2), (255, 255, 0), thickness = 3)

cv.line(blank1, (225, 500), (blank1.shape[1] // 2, blank1.shape[0] // 2), (255, 255, 0), thickness = 3)

#  cv.imshow('Line', blank1)


#  writing texts

cv.putText(blank, 'Hello world!', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

cv.imshow('text canvas', blank)













cv.waitKey(0)