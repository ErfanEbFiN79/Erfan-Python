# You can read about openCV at : https://opencv.org/
# Also you can find install way at : https://opencv.org/get-started/?utm_source=opcv&utm_medium=home
# also you need install caer: add more speed

# first we need to import the library
import cv2 as cv

# for read images and return as a matrix
# ! if you have image it's bigger than your screen size you need to reshape it.
img = cv.imread('D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Images\Cats\Cat1.jpg')

# reading videos
capture = cv.VideoCapture("D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Videos\SampleVideo1.mp4")
# ! 0 mean your web cam
#capture = cv.VideoCapture(0)

# display image
#cv.imshow('Cat1', img)

# ! reading videos is kind of defferent with reading images we need use while loop
while True:
    # read frame and isTrue get we can read a frame or not
    isTrue, frame = capture.read()

    # Display each frame of video
    cv.imshow('Sample_video_1', frame)

    # stop video from playing
    if cv.waitKey(20) & 0xff==ord('d'):
        # 0xff==ord('d') means if we press d on keyborad
        # stop play video
        break

capture.release()
cv.destroyAllWindows()


# wait for key press
cv.waitKey(0)


