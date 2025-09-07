import cv2 as cv

img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')
cv.imshow('Cat 1', img)

# converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

# blur image
Blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur cat", Blur)
Blur2 = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur cat2", Blur2)

# Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Cat Canny', canny)

# Dilating the image
canny = cv.Canny(Blur2, 125,175)
dilated = cv.dilate(canny, (10,10), iterations=5)
cv.imshow('Cat Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Cat Eroded', eroded)

# Resize
resized1 = cv.resize(img, (40,40))
cv.imshow('Cat resized1', resized1)

# Cropping
cropped = img[20: 100, 100:200]
cv.imshow('Cat Cropped', cropped)

cv.waitKey(0)