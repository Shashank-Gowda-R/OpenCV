import cv2 as cv
import numpy as np

img =  cv.imread("photos/cats.jpg")
# cv.imshow("CATS",img)

blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("BLUR",blur)

canny = cv.Canny(blur,125,175)
cv.imshow("CANNY EDGES",canny)

# ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("THRESH",thresh)

contours, hirearchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} These many contours found")

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("CONTOURS DRAW",blank)


cv.waitKey(0)