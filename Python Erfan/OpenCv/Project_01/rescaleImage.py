import cv2 as cv

img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.imshow('Cat1', img)
cv.imshow('Cat1 Resized', rescaleFrame(img, 0.75))

cv.waitKey(0)