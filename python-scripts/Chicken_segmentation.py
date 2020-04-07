# import os
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

def choose_data():
    data_video = filedialog.askopenfile(mode='r')
    root = tk.Tk()
    root.withdraw()
    return data_video.name


def import_video():
    video_name = choose_data()
    cap = cv2.VideoCapture(video_name)
    return cap, video_name

out = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (1920,1080))


cap, video_name = import_video()

while cap.isOpened():
    ret, frame = cap.read()

    # red hens: https://pinetools.com/image-color-picker --> selected hsv colors for red hens

    #blurFrame = cv2.blur(frame, (3, 3))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range1 = np.array([0, 95, 33])
    upper_range1 = np.array([11, 255, 158])

    mask1 = cv2.inRange(hsv, lower_range1, upper_range1)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    closing = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel1)
    erosion1 = cv2.erode(closing, kernel1, iterations=1)
    dilation1 = cv2.dilate(erosion1, kernel1, iterations=2)
    blur = cv2.GaussianBlur(dilation1, (3, 3), 0)
    ret, thresh2 = cv2.threshold(blur, 200, 255, cv2.THRESH_TOZERO)

    redhens=thresh2

    cv2.imshow('mask1', redhens)


    # white hens

    blur2 = cv2.GaussianBlur(frame, (9, 9), 0)
    gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 200, 255, cv2.THRESH_TOZERO)
    whitehens=thresh1

    #cv2.imshow('mask2', whitehens)

    # red hens and white hens binary frames combined

    Together=  cv2.addWeighted(redhens, 1, whitehens, 1, 0)
    #cv2.imshow('Segmented image', Together)

    freem = cv2.cvtColor(Together, cv2.COLOR_GRAY2RGB)
    out.write(freem)  # Save it

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()