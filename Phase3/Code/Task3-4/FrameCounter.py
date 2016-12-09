# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:15:31 2016

Utility function to count the number of frames for video files in a griven directory

@author: Darshan Shetty
"""
import cv2
import os
def countFramesInFolder(folderLocation):
    totalCount=0;
    videoList=os.listdir(folderLocation)
    for video in videoList:
        filePath=os.path.join(folderLocation,video)
        cap = cv2.VideoCapture(filePath)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            totalCount=totalCount+1
        cap.release()
    return totalCount