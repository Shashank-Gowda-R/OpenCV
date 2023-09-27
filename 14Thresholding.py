# Thresholding is binarizing the image, where image will be 0 black or 255 white
import cv2 as cv

img = cv.imread("photos/lady.jpg")
cv.imshow("Lady",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY IMAGE",gray)

# Simple Thresholding
threshold,thresh = cv.threshold(gray,65,255,cv.THRESH_BINARY)
cv.imshow("Simple Threshold Image",thresh)

# Inverse Threshold
threshold,thresh_inv = cv.threshold(gray,65,255,cv.THRESH_BINARY_INV)
cv.imshow("Inverse Threshold",thresh_inv)


# Adapted Thresholding: This is used to find the optimized threshold value by it's self and given the threshold image we don't have to mention the threshold value 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Threshold Image",adaptive_thresh)
# Gaussian is better than mean, las value gives the clarity of the image. If we increase the value we will get the clear image

adaptive_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,5)
cv.imshow("Inverse Adaptive Threshold Image",adaptive_inv)

cv.waitKey(0)