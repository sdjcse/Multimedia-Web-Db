# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:25:16 2016

Utility function to create video files from a given input for a given set of frames.
Input-Input video file name,frame start number, frame end number
Output-Nothing is returned but the the output is saved in the directory containing script
with the name provided

@author: Darshan Shetty
"""
import cv2
import os
def outputProcessor(inputfile,start,end):
    count=0;
    cap = cv2.VideoCapture(inputfile)
    #Unable to use the source fourcc value for the output video
    #due to codec problems. If you are able to incorporate it, please change
    #the code below
    #int(cap.get(cv2.CAP_PROP_FOURCC))
    out = cv2.VideoWriter('temp.avi',cv2.VideoWriter_fourcc(*'XVID'), cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        count=count+1
        if count>=start and count <=end:
            out.write(frame)
        elif count>end:
            break
    cap.release()
    out.release()
    cap = cv2.VideoCapture('temp.avi')
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=cap.get(cv2.CAP_PROP_FPS)
    wait=int( 1/fps * 1000/1 )
    cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
    #This step is not working as expected. Still displays small window.
    #Works better that AUTOSIZE for maximized screen. Initial window however
    #is small
    cv2.resizeWindow("Output",width,height)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if not ret:
            break
        cv2.imshow('Output',frame)
        if cv2.waitKey(wait) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    os.remove('temp.avi')
#outputProcessor('C:\\D-Drive\\studies\\MCS\\MWDB\\Project\\codes\\code\\Phase2_code\\P2DemoVideos\\6x_SQ_BL_TM_BR_Check.mp4',3,18)
