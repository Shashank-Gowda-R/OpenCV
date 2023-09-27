import cv2 as cv

def resizingFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)

# img = cv.imread("photos/cat_large.jpg")

# cv.imshow("CAT",img)
# cv.imshow("RESIZE IMG",resizingFrame(img,scale=0.5))
# cv.waitKey(0)

capture = cv.VideoCapture("videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video",frame)
    resizeFrame = resizingFrame(frame,scale=0.2)
    cv.imshow("resized Video",resizeFrame)

    if(cv.waitKey(12) & 0xFF==ord('d')):
        break

capture.release()
capture.destroyAllWindows()