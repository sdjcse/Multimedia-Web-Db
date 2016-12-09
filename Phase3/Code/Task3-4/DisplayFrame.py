# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:29:16 2016

Utility function to isplay given frame file for input video

@author: Darshan Shetty
"""
import cv2
def displayFrame(inputfile,frameno):
    count=0;
    cap = cv2.VideoCapture(inputfile)
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
    #This step is not working as expected. Still displays small window.
    #Works better that AUTOSIZE for maximized screen. Initial window however
    #is small
    cv2.resizeWindow("Output",width,height)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        count=count+1
        if count == frameno:
            cv2.imshow('Output',frame)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
#displayFrame('D:\\Coursework\\Candan\\phasetwo\\Phase1_inputvideos\\test\\square_L_R.mp4',3)