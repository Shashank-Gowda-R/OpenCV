import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype="uint8")

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank,(200,200),200,255,-1)
cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

# Bitwise AND: Returns intersection

ba = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise AND",ba)

# Bitwise OR
br = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR",br)

# Bitwise XOR: Non intersecting regions, If both are 1 output is zero, anyone is 1 then output is 1
bx = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR",bx)

# Bitwise not
bn = cv.bitwise_not(rectangle)
cv.imshow("Bitwise Not",bn)
bn1 = cv.bitwise_not(circle)
cv.imshow("Bitwise Not",bn1)

cv.waitKey(0)