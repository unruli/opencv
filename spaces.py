import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('shoe.jpg')
cv.imshow('shoe', img) 


# plt.imshow(img)
# plt.show()
#bgr to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#bgr to hsv
HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', HSV)

# bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR  2 RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', RGB)

plt.imshow(RGB)
plt.show()
#HSV TO BGR
HSV_BGR = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', HSV_BGR)





cv.waitKey(0)