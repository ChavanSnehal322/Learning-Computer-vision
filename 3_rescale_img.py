# reduce computer load foor playing high resolution videos
# changing width and height of frame

import cv2 as cv

img = cv.imread('Photos/fullerton-california.jpeg')

cv.imshow('college', img)

#  function to rescale the frame
def rescaleFrame(frame, scale = 0.75):

    # converting float to integer
    width = int( frame.shape[1] * scale)
    height = int( frame.ahape[0] * scale)

    dimen = ( width, height)

    return cv.resize(frame, dimen, interpolation = cv.INTER_AREA)

cv.waitKey(0)