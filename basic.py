import cv2 as cv
img = cv.imread('shoe.jpg')
cv.imshow('shoe', img)


#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny edge', canny,)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized
)

#cropping 
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped )



cv.waitKey(0)