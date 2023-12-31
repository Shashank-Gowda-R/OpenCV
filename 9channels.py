# How to split and merge color channels in OpenCV
import cv2 as cv
import numpy as np

img = cv.imread("photos/park.jpg")
cv.imshow("Original",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

# Splitting
b,g,r = cv.split(img)

cv.imshow("BLUE",b)
cv.imshow("GREEN",g)
cv.imshow("RED",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow("Merged Image",merge)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)


cv.waitKey(0)