import cv2 as cv

#  function to rescale the frame ( image, recorded videos, live videos)
def rescaleFrame(frame, scale=0.75):

    # converting float to integer
    width = int( frame.shape[1] * scale)
    height = int( frame.shape[0] * scale)

    dimen = ( width, height)

    return cv.resize(frame, dimen, interpolation = cv.INTER_AREA)

# function to change resolution of live video only, been captured on device currently
def changeRes(width, height):

    capture.set(3, width)
    capture.set(4, height)
    

# reading videos
capture = cv.VideoCapture('Reading a video Images/Videos/Arrays.mp4')

while True:

    # reading a frame
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Original Video', frame)

    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):

        break

# releases the window
capture.release()

# closes the opened windows
cv.destroyAllWindows()