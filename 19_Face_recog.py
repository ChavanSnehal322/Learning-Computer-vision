import numpy as np

import cv2 as cv

haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

#  list to store the names of the person in training dataset
people = ['Madonna', 'Sam Altman', 'Elon Musk']

# features = np.load('features.npy', allow_pickle= True)
# labels = np.load('labels.npy', allow_pickle= True)

#  instansiating the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
 
face_recognizer.read('faces_recog_trained.yml')

img = cv.imread(r'/Users/snehalchavan/Visual Studio Projects/Open CV learnings/Validatn/images (2).jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

#  detect person face

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for( x, y, w, h ) in face_rect:

    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)

    print(f' label = {people[label]} with a confidence of {confidence} ')

    cv.putText(img, str(people[label] ), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0 ), thickness = 2)

    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)

cv.imshow(' Face detected', img)

cv.waitKey(0)