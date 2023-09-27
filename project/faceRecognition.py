import os
import cv2 as cv
import numpy as np

p=[]
for i in os.listdir("Faces/train"):
    p.append(i)
print(p)

haarCascade = cv.CascadeClassifier("haar_face.xml")
dir = r"C:\Users\Dell\Desktop\OpenCV\project\Faces\train"
features = []
labels = []

def train():
    for person in p:
        path = os.path.join(dir,person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

train()
print("------Training Done------")
print(len(features))
print(len(labels))
features = np.array(features,dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train recognizer on features and labels

face_recognizer.train(features,labels)
np.save("features.npy",features)
np.save("labels.npy",labels)