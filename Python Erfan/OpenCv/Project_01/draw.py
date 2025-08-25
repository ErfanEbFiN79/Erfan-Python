import cv2 as cv
import numpy as np


# create black screen to work with
blank = np.zeros((500,500,3), dtype='uint8')

#img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')
#cv.imshow('Cat1', img)

# we use black screen for drawing insted of cat image
cv.imshow('Black', blank)

#turn all the pixels to the white
white = blank
white[:] = 255,255,255
cv.imshow('White', white)

# Let's create a flag of iran
# 500 / 3 = 166
iran_flag = white
iran_flag[0:166] = 0,255,0
# 166 + 166 = 332
iran_flag[322:500] = 0,0,255
cv.imshow('Iran', iran_flag)


# Let's create a chess ground
blank = np.zeros((500,500,3), dtype='uint8')
chess_ground = blank
W = True
for i in range(500):
    if i % 2 == 0:
        for j in range(500):
            if j % 2 == 0:
                chess_ground[i][j] = 255,255,255
            else:
                chess_ground[i][j] = 0,0,0

    else:
        if j % 2 == 0:
            chess_ground[i][j] = 0,0,0
        else:
            chess_ground[i][j] = 255,255,255

# chess_ground[::2] = 255,255,255
cv.imshow('Chess', chess_ground)

cv.waitKey(0)