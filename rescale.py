import cv2 as cv
img = cv.imread('boootyy.jpg')
cv.imshow('boootyy', img)

def rescaleFrame(frame, scale=0.75):
    #images videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA
    )

resized_image=rescaleFrame(img)
cv.imshow('image',resized_image)

def changeRes(width,height):
    #for live videos 
    capture.set(3,width)
    capture.set(4,height)

#reading videos
capture = cv.VideoCapture('dave.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows

 