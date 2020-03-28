"""
Start image analysis.

This specific script filters chicken-occupied pixels out of snapshots from a given recording and plots them in function
of time.

Sam Willems, Andreas Deturck, Vincent Lacante, Berne Ooms,
Pieter Standaert, Dre Van Hoof, John Heymans, Brecht Grobben

Supervisors: Vere Leybaert, Sara Verlinden, Tomas Norton, Erik Vranken, Meiqing Wang
"""

import cv2
from tkinter.filedialog import askopenfile
import numpy as np


def choose_data():
    data_video = askopenfile(mode='r')
    return data_video.name


def play_video():
    video_name = choose_data()
    cap = cv2.VideoCapture(video_name)

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    play_video()
