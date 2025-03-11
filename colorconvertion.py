import cv2 as cv
import numpy as np
 
image = cv.imread("D:/image_processing/gfggray.png")
 
 


# Convert BGR to HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# # define range of blue color in HSV
# lower_blue = np.array([110,50,50])
# upper_blue = np.array([130,255,255])

# # Threshold the HSV image to get only blue colors
# mask = cv.inRange(hsv, lower_blue, upper_blue)

# # Bitwise-AND mask and original image
# res = cv.bitwise_and(frame,frame, mask= mask)

cv.imshow('image',image)
cv.waitKey(0)

cv.destroyAllWindows()








