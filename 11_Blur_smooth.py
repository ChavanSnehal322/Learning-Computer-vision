#  Blurring and smoothing the img

import cv2 as cv

img = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow('Banner', img)


#  smoothing  = removing the noise from the image ( brightness, camera sensors or lighting )
#  Gaussian blur and other techniques

#  blurring 
# A window/ kernel over a image portion, we have a kernel size ( row X colimn). A blur is applied to middle pixel and the pixels surrounding it
#
#  1] Averaging blur
# Apply th average intensity of all other surrounded pixels in image to the middle pixel
average = cv.blur(img, (3,3))           # passing img and kernel size, increase the kernel size to improve intensity of blur
cv.imshow("Averaging blur img ", average)


# 2] Gaussian Blur
#  Each pixel is given a weight, taking the average of the product of the pixrls weight is assigned to the center pixel
gauss = cv.GaussianBlur(img, (7, 7), 0) # passing img, kernel size and a x parameter
cv.imshow("Gaussian blur", gauss)

# 3] Median blur = effective to remove salt and pepper noise
#
median = cv.medianBlur(img, 3)        # kernel size ( auto considers it as a m X m matrix grid) and 
cv.imshow("Median blur", median)

#  Bilateral Blir
# Applies blur but retaing the image edges

bilateral = cv.bilateralFilter(img, 5, 15, 15)        # passong img, sigma, sigma
cv.imshow("Bilateral blur", bilateral)




cv.waitKey(0)