# Hostogram computation is analysing the distribution of pixel intensity of the image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("photos/cats.jpg")
cv.imshow("Original",img)

# Creating the blank image
blank = np.zeros(img.shape[:2],dtype="uint8")

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

gray = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
cv.imshow("GRAY",gray)

mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("Masked Image",mask)

# Gray Scale Histogram
grayHist = cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Gray Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
plt.plot(grayHist)
plt.xlim([0,256])
plt.show()

# Color Histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)