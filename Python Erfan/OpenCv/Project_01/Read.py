# You can read about openCV at : https://opencv.org/
# Also you can find install way at : https://opencv.org/get-started/?utm_source=opcv&utm_medium=home
# also you need install caer: add more speed

# first we need to import the library
import cv2 as cv

# for read images and return as a matrix
# ! if you have image it's bigger than your screen size you need to reshape it.
img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')

# reading videos
# ! 0 mean your web cam
#capture = cv.VideoCapture(0)

# display image
cv.imshow('Cat1', img)

# wait for key press
cv.waitKey(0)


