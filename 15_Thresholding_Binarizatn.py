#  Thresholding
#  converting a color img to binary image
#  take imag anda threshold value, compare all image pixel with thres value and convert it to binarry image
#  if value < pixel of image intensity = 1 ( 255)
#  else if thres > pixel set intensity to 0

import cv2 as cv

 
img = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow('Banner', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray img', gray)

#  1] Simple thresholding ( Manually pass threshold)

#  thres = binarized img
#  if intensity < threshold = returns same threshold value that is passed
threshold, thres = cv.threshold( gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold img', thres)

#  Inverse thresholded img ( high intensity will be white, white will be converted to black )
threshd, thres_inverse = cv.threshold( gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inverse img', thres_inverse)


#  2] Adaptive thresholding 
#    no need to pass a threshold value, calculates the thres using mean value or gaussian method
#  Allow computer to select a random threshold value

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# src image = gray
# max binarization value = 255
#  method to be used for selecting the threshold
#  threshold type 
#  block size = kernal/ window size to be passed for opencv to use to compute the mean to select the threshold 
#  C value = int subtracted from mean to fine tume the threshold
cv.imshow(' Adaptive thresholding', adaptive_thresh)

#  inverse = converts white pixels to black
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive thresholding inverse', adaptive_thresh_inv)


#  Using gaussian value to find the thres
adaptive_thresh_gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow(' Adaptive thresholding', adaptive_thresh_gaus)
#  Adds weight to each pixel value and calculates the mean for all pixels to get the thres









cv.waitKey(0)
