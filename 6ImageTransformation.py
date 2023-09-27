import cv2 as cv
import numpy as np

img = cv.imread("photos/park.jpg")
cv.imshow("REAL IMAGE",img)

# Translation is basically shifting the images up down left and right

def translation(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = ((img.shape[1]),(img.shape[0]))
    return cv.warpAffine(img,transMat,dimensions)

# -X --> Left
# -Y --> up
# X --> right
# Y --> down

translated = translation(img,0,-100)
cv.imshow("TRANSLATED IMAGE",translated)

# Rotating the images

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    return cv.warpAffine(img,rotMat,(width,height))

rotat = rotate(img,45)
cv.imshow("45 deg",rotat)

rotat2 = rotate(rotat,-45)
cv.imshow("-45 deg",rotat2)

# Flipping

# 0--> Vertical 
# 1--> Horizontal
# -1 --> Both Vertical and Horizontal

flip  = cv.flip(img,0)
cv.imshow("Vertical Flip",flip)

flip  = cv.flip(img,1)
cv.imshow("Horizontal Flip",flip)

flip  = cv.flip(img,-1)
cv.imshow("Both Flip",flip)

# Cropping same as selecting the range in the image pixel matrix

cv.waitKey(0)