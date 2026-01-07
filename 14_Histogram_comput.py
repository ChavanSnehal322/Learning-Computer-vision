
#  Histogram 
#  Computated to find the intensity distribution of the pixels in a image


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
img = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow('Banner', img)

#  grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

circle = cv.circle( blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1 )

mask = cv.bitwise_and( gray, gray, mask = circle )
cv.imshow('mask', mask)

#  1] Gray scale histogram 
gray_hist = cv.calcHist([gray], [0], None, [256] , [0, 256] )
#  image for which histogram is to be displayed
#  channel = 0 
#  mask = if we want histogram for specific portion of img
#  hist size = number of bins to be used to display histogram
#  range = range of all possible pixel values

gray_hist_mask = cv.calcHist([gray], [0], mask, [256] , [0, 256] )


plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel(' # of pixels')
plt.plot(gray_hist)
plt.plot(gray_hist_mask)
plt.xlim([0, 256])

plt.show()          # displays histogram for gray scale image


#  2] Color Histogram

mask_ = cv.circle( blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1 )

masked = cv.bitwise_and( img, img, mask = mask_ )
cv.imshow('masked', masked)


plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel(' # of pixels')
#  tuples of colors channels 
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256] )

    plt.plot(hist, color = col)
    plt.xlim([0, 257])              # setting limit for x axis

plt.show()                          # displays histogram for blue, green and red color





cv.waitKey(0)