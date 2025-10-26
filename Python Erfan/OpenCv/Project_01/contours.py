import cv2 as cv
import numpy as np

img = cv.imread(r'D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\City\NewYork2.jpeg')

cv.imshow('New York', img)

#change it to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray New York', gray)

#edge detected
canny = cv.Canny(img,125,175)
cv.imshow('Canny New York', canny)

#find contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) 
print(f"{len(contours)} contour's found! [canny way]")

# What happend if first we blur the image
blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('New York blur', blur)
canny_blur = cv.Canny(blur,125,175)
contours, hierarchies = cv.findContours(canny_blur,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) 
print(f"{len(contours)} contour's found! [blur canny way]")

# Another way to finding contours insted of canny is threshold let's see it
ret, thresh = cv.threshold(gray,122,255, cv.THRESH_BINARY)
cv.imshow('New York Threshold', thresh)
# Threshold essntially looks at an image and tries to binarize that image.
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)    
print(f"{len(contours)} contour's found! [Threshold way]")


# We want to draw contours at black screen
# Create a black image to work with it
black = np.zeros(img.shape, dtype='uint8')
# draw a contours
cv.drawContours(black,contours, -1, (0,0,255),1)
cv.imshow("contours Drawn", black)

cv.waitKey(0)
