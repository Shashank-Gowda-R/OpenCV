import cv2 as cv

haarCascade = cv.CascadeClassifier("haar_face.xml")

# Face Detection using images
# img = cv.imread("../photos/group 1.jpg")
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Reading the haar_cascade file 
# faces_rect = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
# print(f"Number of faces found = {len(faces_rect)}")
# print(faces_rect)

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imshow("detected Faces",img)

# cv.waitKey(0)

# Face detection using live video
video = cv.VideoCapture(0)

while True:
    isTrue,frame=video.read()
    # cv.imshow("Live Face Detection",frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame,"Face",(x+w-50,y-2),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
        cv.imshow("Live Detection",frame)
    print(f"Number of faces found = {len(face)}")
    if(cv.waitKey(10) & 0xff == ord("d")):
        break

video.release()
cv.destroyAllWindows()