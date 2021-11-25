import cv2 as cv
import numpy as np

img = cv.imread('shoe.jpg')
cv.imshow('shoe', img)

b,g,r = cv.split(img)


cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)


cv.waitKey(0)