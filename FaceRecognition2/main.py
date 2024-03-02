import os
import pickle
import cv2
import face_recognition
import numpy as np
import cvzone


cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

#Import Background
imgBackground = cv2.imread('Resources/background.png')

#Import and load Models
folderModelPath = 'Resources/Modes'
modePath = os.listdir(folderModelPath)
imgModeList = []
for path in modePath:
    imgModeList.append(cv2.imread(os.path.join(folderModelPath,path)))

#Load the encoding folder file
print("Load Encode File...")
file = open('EncodeFile.p','rb')
encodeListKnowWithIds = pickle.load(file)
file.close()
encodeListKnow,studentsIds = encodeListKnowWithIds
print(studentsIds)
print("Encode file loaded...")

while True:

    sucess, img = cap.read()

    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall,faceCurrentFrame)

    imgBackground[162:642, 55:695] = img
    imgBackground[44:677, 808:1222] = imgModeList[0]

    for encodeFace, faceLocation in zip(encodeCurrentFrame,faceCurrentFrame):

        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnow,encodeFace)

        matchIdx = np.argmin(faceDistance)
        print('matchIdx',matchIdx)

        if matches[matchIdx]:
            # print('Know face is detected')
            # print(studentsIds[matchIdx])
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

    #Show image
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)
