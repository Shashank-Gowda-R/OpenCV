# Gradient and Edge Detection. Gradients and Edges are different in mathematical point of view
import cv2 as cv
import numpy as np
img = cv.imread("photos/park.jpg")
cv.imshow("Group Original",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

# Sobel
sobelX = cv.Sobel(gray,cv.CV_64F,1,0)
sobelY = cv.Sobel(gray,cv.CV_64F,0,1)
sobel = cv.bitwise_or(sobelY,sobelX)

cv.imshow("Sobel X",sobelX)
cv.imshow("Sobel Y",sobelY)
cv.imshow("Combined Sobel",sobel)

# Canny: It is more oftenly used but we use sobel for advanced computation
canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)
cv.waitKey(0)