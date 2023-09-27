# Smooth and blur the images, reducing the images by removing the noise
import cv2 as cv

img = cv.imread("photos/cats.jpg")
cv.imshow("Image",img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow("Average Blur",average)

# Gausian Blur: we will get less blur compared to averaging but it is natural, last value is sigmaX value
gaus = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Blur",gaus)

# Median Blur:It is more effective in removing the blur of an image. It is more used in advanced CV project
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

# Bilateral Bluring: It retains the edges of the images
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)