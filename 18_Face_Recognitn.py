#  Recognizing the name of the face detected in the image
#  Using built in image recognizer
#  Training it with the dataset to generate the desired output

import cv2 as cv
import os
import numpy as np


#  list to store the names of the person in training dataset
people = ['Madonna', 'Sam Altman', 'Elon Musk']

p = []

# for i in os.listdir(r'/Users/snehalchavan/Visual Studio Projects/Open CV learnings/Training data'):
#     p.append(i)

# print(p)

#  storing path of training data
DIR = r'/Users/snehalchavan/Visual Studio Projects/Open CV learnings/Training data'

 #  Detecting the images using builtin detection module
#  reading the haarcascade classofoer file to be used for face detection
haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

features = []
labels = []


# # 
# Function to train model
#  iterate through each folder , and image in it 
# Fetch the faces in all those images and train the model  

def create_train():

    for person in people:

        path = os.path.join(DIR, person)

        #  store the index of the name of the person in trainig folder for easier acess of data in numeric form
        label = people.index(person)

        #  iterate through each img in all folders
        for img in os.listdir(path):

            if img.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                img_pth = os.path.join(path, img)
                print(f"Attempting to load image from: {img_pth}")
                
                # Read the image
                img_array = cv.imread(img_pth)

                if img_array is None:
                    print(f"Failed to load image at {img_pth}")
                    continue  # Skip to the next image if loading fails

            # #  each imag path 
            # img_pth = os.path.join(path,img)

            # #  reading the imag from the path
            # img_array = cv.imread(img_pth)

                # converting to gray scale
                gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

                #  rect around faces in img
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=3)

                #  iterating through the faces in rect
                for( x, y, w, h) in faces_rect:

                    #  Cropping the region of interest for faces in img
                    faces_roi = gray[y:y+h, x:x+w]

                    #  appending features and labels in respective list
                    features.append(faces_roi)

                    labels.append(label)


create_train()

# print(f'Length of features = {len(features)}')
# print(f'Length of the labels =  {len(labels)} ')

print("Training is done ...............!!")

# training the face recognizer using the lists of labels and features

#  converting features and labels to numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)

#  instansiating the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#  training the recognizer 
face_recognizer.train(features, labels)

#  save the np array files
np.save('featires.npy', features)
np.save('labels.npy', labels)

#  To use the recoginzer in other file the whole process is to be repeated again

#  OpenCV allows to save the trained model as a .yml file and use it globally when required in other directory, file, proj
face_recognizer.save('faces_recog_trained.yml')














cv.waitKey(0)