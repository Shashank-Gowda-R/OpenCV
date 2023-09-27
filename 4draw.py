import cv2 as cv
import numpy as np 

# To get blank images

blank = np.zeros((500,500,3), dtype='uint8')

# blank[:] = 0,255,0
# # For particular region
# blank[200:300,200:300] = 255,0,0
# cv.imshow("Blank",blank)

# Drawing the Rectangle
# cv.rectangle(blank,(0,0),(400,200),(9,99,199),thickness=-2)
# cv.imshow("Rectangle",blank)

# # Drawing the circle

# cv.circle(blank,((blank.shape[1]//2),(blank.shape[0]//2)),200,(0,255,255),thickness=-1)
# cv.imshow("Circle",blank)

# Drawing line using rectangle function
# cv.rectangle(blank,(50,0),(50,350),(9,99,199),thickness=-2)
# cv.imshow("Rectangle",blank)

# Drawing the Flag

cv.line(blank,(47,100),(47,400),(0,80,190),thickness=5)
cv.rectangle(blank,(50,100),(230,130),(10,100,255),thickness=-1)
cv.rectangle(blank,(50,130),(230,160),(255,255,255),thickness=-1)
cv.rectangle(blank,(50,160),(230,190),(0,255,0),thickness=-1)
cv.circle(blank,(140,145),15,(220,0,0),thickness=-1)
cv.putText(blank,"INDIAN FLAG",(80,400),cv.FONT_HERSHEY_DUPLEX,1.5,(100,100,100),thickness=3)
cv.imshow("Draw",blank)
cv.waitKey(0) 