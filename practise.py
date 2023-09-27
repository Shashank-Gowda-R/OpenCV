import cv2 as cv

video = cv.VideoCapture(0)
while True:
    isTrue, frame = video.read()
    cv.imshow("Live Video",frame)
    if(cv.waitKey(10) & 0xFF == ord("d")) :
        break;

video.release()
cv.destroyAllWindows()