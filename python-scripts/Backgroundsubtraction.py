# import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def choose_data():
    data_video = filedialog.askopenfile(mode='r')
    root = tk.Tk()
    root.withdraw()
    return data_video.name


def import_video():
    video_name = choose_data()
    cap = cv2.VideoCapture(video_name)
    return cap, video_name

video_name = choose_data()
cap = cv2.VideoCapture(video_name)

# Gebruikte sites voor morfologische filters:
# http://www.nitc.ac.in/electrical/ipg/python/opencv-python-tutroals.pdf
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html
# http://amroamroamro.github.io/mexopencv/opencv_contrib/BackgroundSubtractorDemo.html
# https://github.com/kyamagu/mexopencv/blob/master/opencv_contrib/%2Bcv/BackgroundSubtractorGMG.m
# https://docs.opencv.org/3.4/d2/d55/group__bgsegm.html

cap = cv2.VideoCapture(video_name)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)


#gebruikte sites voor video saven: https://stackoverflow.com/questions/28049295/how-to-save-masks-of-videos-in-opencv2-python
#https: // www.learnopencv.com / read - write - and -display - a - video - using - opencv - cpp - python /
#https://stackoverflow.com/questions/29317262/opencv-video-saving-in-python/45868817
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (1920,1080))
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
    out.write(frame)  # Save it

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30) & 0xff
    if keyboard == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

"""
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(35) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""

#https://www.youtube.com/watch?v=nRt2LPRz704 Dit script houdt wel rekening met veranderende achtergrond door history.
"""
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def choose_data():
    data_video = filedialog.askopenfile(mode='r')
    root = tk.Tk()
    root.withdraw()
    return data_video.name

def import_video():
    video_name = choose_data()
    cap = cv2.VideoCapture(video_name)
    return cap, video_name

video_name = choose_data()
cap = cv2.VideoCapture(video_name)

subtractor = cv2.createBackgroundSubtractorMOG2(history=20, detectShadows=True)
while True:
    _, frame = cap.read()
    mask = subtractor.apply(frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
"""


"""
This manual code will not adapt when the background changes, it just focuses on the first frame. 
https://www.youtube.com/watch?v=nRt2LPRz704

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)

    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
"""
