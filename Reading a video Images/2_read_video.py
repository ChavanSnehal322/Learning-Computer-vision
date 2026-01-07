import cv2 as cv

# running existing video from path
capture = cv.VideoCapture('Reading a video Images/Videos/Arrays.mp4')        # binary values if webcam is connected

# dusplaying video as a frames
while True:

    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # id d is pressed the video is stopped
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()