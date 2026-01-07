
# 
import cv2 as cv        

# takes a paths of image and returns a image as a matrix of pixels
img = cv.imread('Reading a video Images/Photos/images.jpeg')

# Displaying the image using cv.imshow ( name of window , matrix of pixels to be displayed)
cv.imshow('building', img)

# 
cv.waitKey(0)

