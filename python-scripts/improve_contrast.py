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


def choose_data():
    data_video = askopenfile(mode='r')
    return data_video.name


def import_video():
    video_name = choose_data()
    cap = cv2.VideoCapture(video_name)
    return cap


def improve_contrast():

    cap = import_video()

    while cap.isOpened():
        ret, frame = cap.read()

        # Converting image to LAB Color model
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        # Splitting the LAB image to different channels
        l, a, b = cv2.split(lab)

        # Applying CLAHE to L-channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)

        # Merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl, a, b))

        # Converting image from LAB Color model to RGB model
        final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        cv2.imshow('Improved contrast', final)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    improve_contrast()
