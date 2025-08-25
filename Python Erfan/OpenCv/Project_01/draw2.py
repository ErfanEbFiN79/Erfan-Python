import cv2 as cv
import numpy as np

# create black screen to work with
black = np.zeros((500,500,3), dtype='uint8')

# we use black screen for drawing insted of cat image
cv.imshow('Black', black)

# draw a squre
black[100:300, 300:400] = 0,0,255
cv.imshow('Black with red', black)

# draw a rectangle
black = np.zeros((500,500,3), dtype='uint8')
cv.rectangle(black,(0,0),(400,400),(0,255,0),5)
cv.imshow('Rectangle', black)

# draw a rectangle full color
black = np.zeros((500,500,3), dtype='uint8')
cv.rectangle(black,(0,0),(black.shape[1]//2,black.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# cv.FILLED = -1
cv.imshow('Rectangle full', black)

# draw a circle
black = np.zeros((500,500,3), dtype='uint8')
cv.circle(black,(black.shape[1]//2,black.shape[0]//2),radius=black.shape[1]//2,color=(0,0,255),thickness=-1)
cv.circle(black,(black.shape[1]//2,black.shape[0]//2),radius=black.shape[1]//2 - 10 ,color=(255,255,255),thickness=8)
cv.imshow('Circle', black)

# draw a line
cv.line(black,(60,255),(440,255),(255,255,255),80)
cv.imshow('Line', black)

# write text
text = 'stop'
cv.putText(black,'STOP',(250 - (len(text)*10),265),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),1)
cv.imshow('Text', black)

cv.waitKey(0)