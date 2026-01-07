
import cv2 as cv
import numpy as np

img  = cv.imread('Reading a video Images/Photos/images.jpeg')

cv.imshow('images.jpeg', img)

# 1. Translation = shifting the image along x axis to y axis and vice versa

#  x and y are the pixels to be shifted in the image to perform translation
def translate(img, x, y):
    
    #  creating the tuple for the image
    transMat = np.float32([[1, 0, x], [0, 1, y] ])

    dim = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dim)

# # x = right
# # y = down
# -x = left
# -y = up

#  moving the image by 100 pixels to right and down ( img , x , y )
translated = translate(img, 100, 100)

#  image move down by the co ordinates mentioned and displays black pixels on the original moved part
cv.imshow("Translated img ", translated)

#  moving the image by 100 pixels to left and down ( img , x , y )
translated1 = translate(img, -100, 100)

#  image move down by the co ordinates mentioned and displays black pixels on the original moved part
cv.imshow("Translated img ", translated1)


# 2. Rotation = rotating image by and angle as any refernce rotation point in the image
def rotate( img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    #  matrix to rotate the imahe at a point and angle 
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    diam = (width, height)

    return cv.warpAffine(img, rotMat, diam)

#  rotate image by 45 degrees in clockwise direction
rotated = rotate(img, 45)
cv.imshow('Rotated img', rotated)

#  rotate image by 55 degrees in anti clockwise direction
rotated1 = rotate(img, -55)
cv.imshow('Anto clck Rotated img', rotated1)

#  rotate a previously rotated image
rotated_rotate = rotate(rotated, -55)
cv.imshow('Rotated rotated img', rotated_rotate)

#  3 . Resizing image
resized = cv.resize( img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized_cubic img', resized)

# 4. Flipping image
flip = cv.flip( img, 0)
#  0 = vertical flip ( across x axis)
#  1 = Horizontally ( y axis)
#  -1 = Both vertical & horizontal ( x and y axis)

cv.imshow("Flipped vertically", flip)

flip1 = cv.flip( img, -1)
cv.imshow("Flipped both vert and horiz", flip1)

#  5. Cropping image

cropped = img[200: 400, 300: 400]        # slicing the image
cv.imshow('cropped img', cropped)


cv.waitKey(0)