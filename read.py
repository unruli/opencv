  import cv2 as cv

# img = cv.imread('photos\shoe.jpg')
 
# cv.imshow("gyal", img)
#Reading videos
capture = cv.VideoCapture('videos/video 1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video')

cv.waitKey(0) 