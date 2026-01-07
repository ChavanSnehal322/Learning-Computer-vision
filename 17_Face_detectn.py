
#  detecting faces in the image/ video

import cv2 as cv

img = cv.imread('Reading a video Images/Photos/person1.jpeg')
cv.imshow('Person', img)

#  converting img to grayscale, Harcascade do not use skin color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale img', gray)


img1 = cv.imread('Reading a video Images/Photos/Humans.jpeg')
cv.imshow('Humans', img1)

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale img', gray1)
 
#  reading the haarcascade classofoer file to be used for face detection
haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

#  detecting the face in the image using the haarcascade model
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=2)
#  scalefactor = scale of rect
#  minNeighbor = no. of neighbors the rect to be. called as a face
#  returns list of the co ordinates of the faces rectangle in the img

#  printing the list of rect co ordinates
print( f'Number of faces in the img = {len(faces_rect)}')

#  loop over list over the co ordinates of the faces and drawing rect for all of them

for( x, y, w, h) in faces_rect:

    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow('Detected faces in img', img)

#  printing rect for img1
face_rect = haar_cascade.detectMultiScale(gray1, scaleFactor= 1.1, minNeighbors=0)
#  printing the list of rect co ordinates
print( f'Number of faces in the img1 = {len(face_rect)}')

for( x, y, w, h) in face_rect:

    cv.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces in img', img1)

#  sensitive to noise so can predict incorrect number of faces in the groups of people

#  minimizing the noise in the img by modifying scalefactore and minimum Neighbours


#  DLibs face recognizer is more effecttive in detecting faces and mostly used in advanced prjects




cv.waitKey(0)