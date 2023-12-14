import cv2
import numpy as np

height=1400
width=1600

blank_image = np.zeros((height,width,3), np.uint8)

blank_image[:,0:width] = (255,255,255)      # (B, G, R)
# blank_image[:,width//2:width] = (0,255,0)


# cv2.imshow("A New Image", blank_image)
cv2.imwrite("blank.jpg", blank_image)

cv2.waitKey(0)

