import cv2 as cv
import numpy as np

img = cv.imread(r'D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\City\NewYork2.jpeg')
cv.imshow('New York', img)

# Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
cv.imshow('New York translated1', translated)

cv.waitKey(0)