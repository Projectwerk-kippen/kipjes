"""
Start image analysis.

This specific script filters chicken-occupied pixels out of snapshots from a given recording and plots them in function
of time.

Sam Willems, Andreas Deturck, Vincent Lacante, Berne Ooms,
Pieter Standaert, Dre Van Hoof, John Heymans, Brecht Grobben

Supervisors: Vere Leybaert, Sara Verlinden, Tomas Norton, Erik Vranken, Meiqing Wang
"""

# import os
import cv2
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


def enhance_video():
    cap, video_name = import_video()

    # width = int(cap.get(3))
    # height = int(cap.get(4))

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # out = cv2.VideoWriter((os.path.split(video_name)[-1] + '_enhanced.avi'), fourcc, 20, (height, width), 0)

    while cap.isOpened():
        ret, frame = cap.read()

        # Applying Gaussian low-pass filter to remove noise
        blur = cv2.GaussianBlur(frame, (21, 21), 0)

        # Converting image to LAB Color model
        lab = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)

        # Splitting the LAB image to different channels
        l, a, b = cv2.split(lab)

        # Applying CLAHE to L-channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)

        # Merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl, a, b))

        # Converting image from LAB Color model to grayscale model for thresholding
        contrasted = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        gray = cv2.cvtColor(contrasted, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Result', gray)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    enhance_video()
