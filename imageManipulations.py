# playing with OpenCV in Python...

import cv2
import numpy as np

print('Loading image...')
input = cv2.imread('./pitsikisseslexie.jpg')
originalImage = input
height = input.shape[0]
width = input.shape[1]
grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

verticalScaleFactor = 900.0/height
horizontalScaleFactor = 1440.0/width

print('Horizontal factor:',  horizontalScaleFactor)
print('Vertical factor:',  verticalScaleFactor)
scaleFactor = min(verticalScaleFactor, horizontalScaleFactor)
print('minimum to be used is:', scaleFactor)



output = cv2.resize(grayscaleImage,(0,0), fx = scaleFactor, fy=scaleFactor)

cv2.imshow('Very nice', output)
cv2.waitKey(0)
cv2.destroyAllWindows()



