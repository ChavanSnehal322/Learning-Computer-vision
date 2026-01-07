import cv2 as cv

img = cv.imread('Reading a video Images/Photos/images.jpeg')

cv.imshow('imag', img)

#  convert the colored image to a greay scaled image
gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



#  blur the image
blur = cv.GaussianBlur( img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#  convert the image to a edges of the objects in image
canny = cv.Canny(img, 125, 170 )
cv.imshow('Canny edges image', canny)

#  cascade the edges - blur the image and  by canny function to reduce the unwanted edges in image
ca = cv.Canny( blur, 125, 170)
cv.imshow('canny cascade edges', ca)

#  dilating the images - increase the edge weight 
dilated = cv.dilate( ca, (7, 7), iterations = 4)
cv.imshow('Dilated', dilated)

#  erode - getting back the edge of image same as canny cascade by using dilated image
eroded = cv.erode( dilated, (7, 7), iterations= 3)
cv.imshow('eroded', eroded)

#  resize the image - display the image in a frame of size (,) ignoring the aspect ratios
# cv.INTER_AREA - shrink the image
# INTER_CUBIC - high resolution image is generated 
resized = cv.resize( img, ( 500, 500), interpolation= cv.INTER_AREA)
cv.imshow('Resized img', resized)

#  cropping the image
cropped = img[50: 200, 200: 400]
cv.imshow('cropped img', cropped)

cv.waitKey(0)