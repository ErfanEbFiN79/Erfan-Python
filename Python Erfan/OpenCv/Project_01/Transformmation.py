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

#Rotation
def rotate(img, angle, rotationPoint=None):
    (hight,width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width//2, hight//2)
    
    rotMat = cv.getRotationMatrix2D(rotationPoint,angle,1.0)
    dimentions = (width,hight)

    return cv.warpAffine(img,rotMat, dimentions)

rotated = rotate(img,45)
cv.imshow('New York rotate_01', rotated)

#Resizing

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('New York resized_01', resized)

#Flipping
flip = cv.flip(img,flipCode=0)
# You can use 0,1 and -1 for flip code
cv.imshow('New York flip', flip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('New York cropped', cropped)


cv.waitKey(0)