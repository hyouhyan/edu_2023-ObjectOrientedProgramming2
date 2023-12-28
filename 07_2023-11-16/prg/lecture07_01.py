#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from my_module.k22047.lecture07_01_module import get_masked_image

def lecture07_01():

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (640,480))
        masked_frame = get_masked_image(resized_frame)

        cv2.imshow('frame', masked_frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break # 'ESC' key is pressed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    lecture07_01()