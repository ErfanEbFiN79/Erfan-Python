import cv2 as cv

capture = cv.VideoCapture("D:\Erfan-Python\Python Erfan\OpenCv\Project_01\Videos\SampleVideo1.mp4")

def rescaleFrame(frame, scale = 0.5):

    # this method is work for images, videos and live videos

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # just work for live video
    capture.set(3,width)
    capture.set(4, height)


while True:
    # read frame and isTrue get we can read a frame or not
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    # Display each frame of video
    cv.imshow('Sample_video_1', frame)
    cv.imshow('Sample_video_1_resized', frame_resized)

    # stop video from playing
    if cv.waitKey(20) & 0xff==ord('d'):
        # 0xff==ord('d') means if we press d on keyborad
        # stop play video
        break

capture.release()
cv.destroyAllWindows()