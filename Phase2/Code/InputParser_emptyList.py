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
def splitStrToNumList(string):
    return [float(x) for x in string.split(',')]


def parseInput(formatDict):
    masterList=[]
    prevData=[-1,-1,-1]
    framecount=0
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
                        framecount=0 #Added to accomodate empty frames
                if(prevData[1]!=frameno):
                    framecount=framecount+1 #Added to accomodate empty frames
                    if(prevData[0]==video):
                        #Removed to accomodate empty frames
                     """frameDataList.append(cellDataList)
                     videoDataList.append(frameDataList)
                     cellDataList=[]
                     frameDataList=[]"""
                     #Added to accomodate empty frames
                     frameDataList.append(cellDataList)
                     videoDataList.append(frameDataList)
                     cellDataList=[]
                     frameDataList=[]
                     while(framecount<int(frameno)):
                            videoDataList.append([])
                            framecount=framecount+1

                if(prevData[2]!=cellno):
                    if(prevData[1]==frameno):
                     frameDataList.append(cellDataList)
                     cellDataList=[]
                cellDataList.append(splitStrToNumList(data))    #Changed
                prevData[0]=video
                prevData[1]=frameno
                prevData[2]=cellno
    frameDataList.append(cellDataList)
    videoDataList.append(frameDataList)
    masterList.append(videoDataList)
    #print(masterList)
    return masterList

def getCHist():
    return parseInput({'fileName':'inputVideos\\out_file.chst','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getSift():
    return parseInput({'fileName':'inputVideos\\out_file.sift','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getMVect():
    import processMvect
    processMvect.filterMvect()
    return parseInput({'fileName':'inputVideos\\out_file.mvect.filtered','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getCHistPCA():
    return parseInput({'fileName':'inputVideos\\out_file_d.cpca','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getSiftPCA():
    return parseInput({'fileName':'inputVideos\\out_file_d.spca','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getMVectPCA():
    return parseInput({'fileName':'inputVideos\\out_file_d.mpca','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getCHistKM():
    return parseInput({'fileName':'inputVideos\\out_file_d.ckm','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getSiftKM():
    return parseInput({'fileName':'inputVideos\\out_file_d.skm','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

def getMVectKM():
    return parseInput({'fileName':'inputVideos\\out_file_d.mkm','filePos':0,'framePos':1,'cellPos':2,'dataPos':3})

#x= (getMVect())
#print len(x[40])

