#playing with image processing

#first thing - make sure opencv3 is installed
import cv2
import numpy as np
# import matplotlib
from matplotlib import pyplot as plt

#load my favorite picture (one of them, at least)
img_filename = '/Users/kwittmann/Pictures/Habubus.jpg'
img_color = cv2.imread(img_filename, 1)
img_colorWithAlpha = cv2.imread(img_filename, -1)
img_grayscale = cv2.imread(img_filename,cv2.IMREAD_GRAYSCALE)
# can use presets for param: Color is 1, grayscale is 0, and the unchanged is -1.
# unchanged (-1) keeps alpha channel
print ('Shape of grayscale image is', img_grayscale.shape)
print ('Shape of color image is', img_color.shape)
print ('Shape of alpha image is', img_colorWithAlpha.shape)

# playing with histograms...
colorChannel = 0
histSize = [256] # try playing with this for larger bins
histRange = [0, 256]
histogram = cv2.calcHist([img_color], [colorChannel], None, histSize, histRange)
plt.hist(img_color.ravel(), 256, histRange)
plt.show()

colorChannels = ('b', 'g', 'r')

for i, col in enumerate(colorChannels):
	histogram2 = cv2.calcHist([img_color], [i], None, histSize, histRange)
	plt.plot(histogram2, color = col)
	plt.xlim(histRange)

plt.show()

plt.imshow(img_grayscale, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) #hide ticks
quarterHeight = img_grayscale.shape[0]/4
quarterWidth = img_grayscale.shape[1]/4
xVector = [quarterWidth, 2*quarterWidth, 3*quarterWidth, 2*quarterWidth, quarterWidth]
yVector = [2*quarterHeight, quarterHeight, 2*quarterHeight, 3*quarterHeight, 2*quarterHeight]
plt.plot(xVector,yVector,'m', linewidth=5)
plt.show()

#show picture on screen with title
# cv2.imshow('Habubu and Abu Habubu', img_grayscale)
# wait for a key, then close the image window
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print ("Thanks, hope you enjoyed yourself... ")