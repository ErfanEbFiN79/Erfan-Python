import cv2 as cv

img = cv.imread(r'D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\City\NewYork2.jpeg')

cv.imshow('New York', img)

#change it to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray New York', gray)

#edge detected

canny = cv.Canny(img,125,175)
cv.imshow('Canny New York', canny)

#find contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 


cv.waitKey(0)
