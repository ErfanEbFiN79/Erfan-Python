import cv2 as cv

img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')
cv.imshow('Cat 1', img)

# converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

cv.waitKey(0)