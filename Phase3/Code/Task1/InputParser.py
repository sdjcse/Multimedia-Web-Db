# -*- coding: utf-8 -*-
"""
Utility Function to parse output obtained from Phase 1. Function returns a master
list where each entry is in turn a list containing the output data for each cell
in every frame of the video.
MasterList:[List of video data]-Each row has data for a video
[Video Data]-[List of frame data]Each row has data for frames in the video
[Frame Data]-[List of cell data]Each row contains values for cells in the frame
[Cell Data]-[List of feature data] Each row is a feature found in the data based
            on the type of file given

Input: dict in the format {"fileName":"abc","filePos":0,"framePos":1,"cellPos":2,
                           "dataPos":3}
Output: list containing data aforementioned

Uncomment print at the end to look at the data here only

@author: Darshan Shetty
"""
import os
from os.path import dirname

def parseInput(formatDict):
    masterList=[]
    prevData=[-1,-1,-1]
    frameDataList=[]
    cellDataList=[]
    fileToParse=formatDict['fileName']
    with open(fileToParse,'r') as file:
        for line in file:
            if line:
#Remove all spaces in the line so that easier to use for others
                line=line.strip()
                line=line.replace(" ","")
                dataInLine=line.split(';')
                video=dataInLine[formatDict['filePos']]
                frameno=dataInLine[formatDict['framePos']]
                cellno=dataInLine[formatDict['cellPos']]
                data=dataInLine[formatDict['dataPos']]
                if(prevData[0]!=video):
                    if(prevData[0]==-1):
                        videoDataList=[]
                    else:
                        frameDataList.append(cellDataList)
                        videoDataList.append(frameDataList)
                        masterList.append(videoDataList)
                        videoDataList=[]
                        frameDataList=[]
                        cellDataList=[]
                if(prevData[1]!=frameno):
                    if(prevData[0]==video):
                     frameDataList.append(cellDataList)
                     videoDataList.append(frameDataList)
                     cellDataList=[]
                     frameDataList=[]
                if(prevData[2]!=cellno):
                    if(prevData[1]==frameno):
                     frameDataList.append(cellDataList)
                     cellDataList=[]
                cellDataList.append(data)
                prevData[0]=video
                prevData[1]=frameno
                prevData[2]=cellno
    frameDataList.append(cellDataList)
    videoDataList.append(frameDataList)
    masterList.append(videoDataList)
    #print len((masterList))
    return masterList

def getPathToInputVideos(filename):
    currentPath=os.getcwd()
    parent=dirname(currentPath)
    inputVideoPath=os.path.join(parent,"inputVideos",filename)
    return inputVideoPath

def getCHist(path):
    return parseInput({'fileName':path,'filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getSift(path):
    return parseInput({'fileName':path,'filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getMVect(path):
    return parseInput({'fileName':path,'filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

