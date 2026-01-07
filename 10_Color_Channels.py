#  R, B, G channels

#  taking the image and splitting to 3 channnels 

import cv2 as cv
import numpy as np

img  = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow("Banner", img)

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
#  dark color signify that the specific color pixel is not present 
#  light color represents that the color pixel is present

print(img.shape) # represents image dimension and color channel number
print(b.shape)
print(g.shape)
print(r.shape)

#  merging the color channels
merged = cv.merge([b,g,r])
cv.imshow("Merged_channels", merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])          # prints img with blue color pixel intensity
green = cv.merge([blank, g, blank])          # prints img with green color pixel intensity
red = cv.merge([blank, blank, r])           # prints img with red color pixel intensity
#  merging the splitted channels to the img
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


cv.waitKey(0)