import cv2 as cv

# Converting into GRAY color
img = cv.imread("photos/lady.jpg")
cv.imshow("COLOR IMAGE",img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("GRAY IMAGE",gray)

# BLUR an image

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("BLUR",blur)

# Edge Cascading

canny = cv.Canny(blur,125,175)
cv.imshow("EDGES",canny)

# Dilating the image
dilated = cv.dilate(canny,(3,3),iterations=2)
cv.imshow("DILATED",dilated)

# ERODING THE IMAGES
eroded = cv.erode(dilated,(7,7),iterations=4)
cv.imshow("ERODED",eroded)

# Resizing the images
resize = cv.resize(img,(250,250),interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZED",resize)

# CROPPING THE IMAGES
crop = img[50:200,150:500]
cv.imshow("CROPPED",crop)

cv.waitKey(0)