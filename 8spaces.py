# Switch between color spaces
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("photos/park.jpg")
cv.imshow("Original",img)
# plt.imshow(img) # RGB image color inversion
# plt.show()

# BGR to Gray
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

# Gray to BGR
# bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# cv.imshow("BGR from GRAY",bgr)

# BGR TO HSV (Hue Saturation Value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsv)

# HSV to BRG
# hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow("HSV TO BGR",hsv_bgr)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB Image",lab)
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("LAB TO BGR",lab_bgr)

# BGR to RGB
# rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("RGB Img",rgb)
# plt.imshow(rgb) # RGB image
# plt.show()

cv.waitKey(0)