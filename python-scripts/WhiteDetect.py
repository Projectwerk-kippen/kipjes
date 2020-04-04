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

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white=np.array([[0, 0, 180]])
    white=np.array([[180, 30, 255]])

    white_mask=cv2.inRange(hsv, lower_white, white)

    (contours,_) = cv2.findContours(white_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if(area > 1000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),10)

    cv2.imshow("tracking", frame)

    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()