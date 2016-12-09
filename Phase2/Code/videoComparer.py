#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     05/10/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#---------------------------o
from munkres import Munkres
from distancemeasure import distanceMeasures
import timeit
import sys
import numpy

hungarianThreshold=5

"""def measureType(metricFunction):
    metricType=""
    dm=distanceMeasures()
    if metricFunction==dm.cosineSimilarity or metricFunction==dm.intersectionSimilarity:
        metricType="Similarity Measure"
    else:
        metricType="Distance Measure"
    return metricType"""


def greedyMunkres(vrMatrix,noOfRows,noOfCols):
    transposeFlag=0
    if noOfRows>noOfCols:
        vrMatrix=numpy.transpose(vrMatrix)
        noOfRows,noOfCols=noOfCols,noOfRows
        transposeFlag=1
    ret_assignments=[]
    #assignedRows={}
    assignedCols={}
    for i in range(0,noOfRows):
        minimum=sys.maxsize
        tempAssignment=None
        for j in range(0,noOfCols):
            if (not assignedCols.has_key(j)) and vrMatrix[i][j]<minimum:
                minimum=vrMatrix[i][j]
                tempAssignment=(i,j)
        assignedCols[tempAssignment[1]]=1
        ret_assignments.append(tempAssignment)
        if len(assignedCols.keys())>=noOfCols:
            break
    if transposeFlag==1:
        for i in range(0,len(ret_assignments)):
            x,y=ret_assignments[i]
            ret_assignments[i]=y,x
        #vrMatrix=numpy.transpose(vrMatrix)
    return ret_assignments



def calcSimilarityWrapper(vector1,vector2,distanceMeasureFunction):
    #metricType=measureType(distanceMeasureFunction)
    """vectorTok1=vectorStr1.split(",")
    vectorTok2=vectorStr2.split(",")
    vector1=[]
    vector2=[]
    for i in range(0,len(vectorTok1)):
        vector1.append(float(vectorTok1[i]))
        vector2.append(float(vectorTok2[i]))"""
    value=distanceMeasureFunction(vector1,vector2)
    similarity=0.0
    if "Similarity" in metricType:
        similarity=(-1)*value
    else:                           #Converting dist to similarity
        similarity=(-1)/(1+value)
    #Converting to negative is done for the Hungarian algo to find the maximum
    return similarity

def initializeMatrix(noOfRows,noOfCols):
    matrix=[]
    for i in range(0,noOfRows):
        eachCol=noOfCols*[0.0]
        matrix.append(eachCol)
    return matrix

def findMinAssignmentPath(matrix,indices): #Actually finds the maximum as the values are negated
    sum=0.0
    for row,col in indices:
        sum+=matrix[row][col]
    return sum

def findMeanSimilarity(value,nvr1,nvr2):
    #minDims=min(nvr1,nvr2)
    maxDims=max(nvr1,nvr2)
    overallSimilarity=value/maxDims #(Equal to (value/minDims)*(minDims/maxDims))
    return overallSimilarity

def compareCells(cellVrList1,cellVrList2,distanceMeasureFunction):
##cellVrList1 and cellVrList2 are list of vectors (only 1 vector in case of color hist) of 2 frames of 2 videos
    noOfVrsC1=len(cellVrList1)
    noOfVrsC2=len(cellVrList2)
    """if min(noOfVrsC1,noOfVrsC2)/max(noOfVrsC1,noOfVrsC2)<0.3:
        return 0.0"""
    vrComparisionMatrix=initializeMatrix(noOfVrsC1,noOfVrsC2)
    #start=timeit.default_timer()
    for i in range(0,noOfVrsC1):
        for j in range(0,noOfVrsC2):
            vrComparisionMatrix[i][j]=calcSimilarityWrapper(cellVrList1[i],cellVrList2[j],distanceMeasureFunction) #distanceMeasureFunction(cellVrList1[i],cellVrList2[j])
            """if vrComparisionMatrix[i][j]==-1:
                break"""
            #One of the distance/similarity Methods dist=(1/(-similarity))-1) similarity=(-1)/(1+dist),negative values for similarity is expected
    #end=timeit.default_timer()
    #t1=end-start
    vrAssignmentList=[]
    if max(noOfVrsC1,noOfVrsC2)>=hungarianThreshold:
        vrAssignmentList=greedyMunkres(vrComparisionMatrix,noOfVrsC1,noOfVrsC2)
    else:
        hungarianAlgo=Munkres()
        #start=timeit.default_timer()
        vrAssignmentList=hungarianAlgo.compute(vrComparisionMatrix)
        #end=timeit.default_timer()
        #t2=end-start
        #print str(noOfVrsC1)+","+str(noOfVrsC2)+","+str(t1)+","+str(t2)+","+str(float(t2/t1))
    totalDistance=findMinAssignmentPath(vrComparisionMatrix,vrAssignmentList)
    overallSimilarity=findMeanSimilarity(totalDistance,noOfVrsC1,noOfVrsC2)
    return overallSimilarity

def compareFrames(frameMat1,frameMat2,distanceMeasureFunction):
##frameMat1 is the ith frame of video1 and frameMat2 is the jth frame of video 2 as passed from the compareVideos function
##This function compares 2 frames by comparing their cells and returns the minimum possible distance between them using the Hungarian Algorithm
    noOfCellsF1=len(frameMat1)
    noOfCellsF2=len(frameMat2)
    if noOfCellsF1==0 or noOfCellsF2==0:
        return 0.0
    cellwiseSimilarityMatrix=initializeMatrix(noOfCellsF1,noOfCellsF2)
    for i in range(0,noOfCellsF1):
        for j in range(0,noOfCellsF2):
            cellwiseSimilarityMatrix[i][j]=compareCells(frameMat1[i],frameMat2[j],distanceMeasureFunction)
    #Match only corresponding cells
    """for i in range(0,noOfCellsF1):
            cellwiseSimilarityMatrix[i][i]=compareCells(frameMat1[i],frameMat2[i],distanceMeasureFunction)"""
    hungarianAlgo=Munkres()
    #start=timeit.default_timer()
    cellAssignmentList=hungarianAlgo.compute(cellwiseSimilarityMatrix)
    #end=timeit.default_timer()
    #t2=end-start
    #print str(noOfCellsF1)+","+str(t2)+",-1"
    totalDistance=findMinAssignmentPath(cellwiseSimilarityMatrix,cellAssignmentList)
    overallSimilarity=findMeanSimilarity(totalDistance,noOfCellsF1,noOfCellsF2)
    #return totalDistance
    return abs(overallSimilarity) #Don't need the negative value anymore

def highestSimilarityMatch(framewiseSimilarityMatrix,noOfRows,noOfCols):
    DPMatrix=initializeMatrix(noOfRows+1,noOfCols+1)
    for i in range(1,noOfRows+1):
        for j in range(1,noOfCols+1):
            DPMatrix[i][j]=framewiseSimilarityMatrix[i-1][j-1] #Copy entries to from the original matrix to the new matrix so as to not break anything
    #DP Part separate so that changes can be made if needed
    for i in range(1,noOfRows+1):
        for j in range(1,noOfCols+1):
            DPMatrix[i][j]=max(DPMatrix[i-1][j-1]+DPMatrix[i][j],DPMatrix[i][j-1]) #seems like DPMatrix[i-1][j] not needed
                #Slow motion other way testing
                #DPMatrix[i][j]=max(DPMatrix[i-1][j-1]+DPMatrix[i][j],DPMatrix[i][j-1],DPMatrix[i-1][j])
    similarityValue=DPMatrix[noOfRows][noOfCols]
    i=noOfRows
    j=noOfCols
    path=[]
    while i>0 and j>0: #j>0 for test
        if DPMatrix[i][j]>DPMatrix[i][j-1]: # Video1's i and Video 2's j th frames were mapped
        #if DPMatrix[i][j]>max(DPMatrix[i][j-1],DPMatrix[i-1][j]): #Slow motion other way testing
            m=[i-1,j-1] #Because in the original matrix is less by 1 row and column
            path.append(m)
            i-=1
            j-=1
            # Remove if needed
            """elif DPMatrix[i][j]==DPMatrix[i-1][j]:
                i-=1"""
        else:
            j-=1
    path.reverse()
    end=path[len(path)-1][1]
    start=path[0][1]
    return (start,end,similarityValue)

def compareVideos(videoFrameMat1,vid1StartFrameNo,vid1EndFrameNo,videoFrameMat2,vid2StartFrameNo,vid2EndFrameNo,distanceMeasureFunction,metric_type,taskNo):
##VideoFrameMat1 and VideoFrameMat2 are 4-D matrices of the form (FrameNo,CellNo,Vectors) and
## Vectors is a 2-D (1 or n*1 for Color Histogram) matrix with each vector
##viz. chst,cpca,ckm,sift,spca,skm,mvect,mpca,mkm
##Each vector is a line in the output files we have and of the form cellNo,line
##if taskNo is even (2,4) return the matching one and a distance measure
    #print vid1EndFrameNo,vid1StartFrameNo,vid2EndFrameNo,vid2StartFrameNo
    #metricType=measureType(distanceMeasureFunction)
    global metricType
    metricType=metric_type
    video1Matrix=videoFrameMat1[vid1StartFrameNo:vid1EndFrameNo+1] #Done to extract specified frames. Can be used for task2
    video2Matrix=videoFrameMat2[vid2StartFrameNo:vid2EndFrameNo+1]
    noOfRows=vid1EndFrameNo-vid1StartFrameNo+1
    noOfCols=vid2EndFrameNo-vid2StartFrameNo+1
    #print noOfRows,noOfCols
    if noOfRows>noOfCols: #Swapping in order to make the video with more frames as the first one
        # For task 2,4 make sure this condition doesn't even get executed
        (video1Matrix,video2Matrix)=(video2Matrix,video1Matrix)
        (noOfRows,noOfCols)=(noOfCols,noOfRows)

    framewiseSimilarityMatrix=initializeMatrix(noOfRows,noOfCols)
    for i in range(0,noOfRows):
        for j in range(i,noOfCols-noOfRows+1+i): #Old (0,noOfCols)
            #To map each frame to every other frame, if no of frames is the same, i.e. noOfRows=noOfCols, then it will be a diagonal matrix
            framewiseSimilarityMatrix[i][j]=compareFrames(video1Matrix[i],video2Matrix[j],distanceMeasureFunction)
    (start,end,totalVal)=highestSimilarityMatch(framewiseSimilarityMatrix,noOfRows,noOfCols)
    minValue=totalVal/(end-start+1) #Value corresponding to the sub-frames alone, more than maxValue
    maxValue=totalVal/noOfCols    #Value for whole video
    #print "Final:"+str(maxValue)+","+str(minValue)
    #print metricType
    if  "Distance" in metricType: #To convert the similarity value to distance value
        minValue=1.0/minValue-1
        maxValue=1.0/maxValue-1
    if taskNo%2!=0: #For tasks 1 and 3 we need only maxValue
        return maxValue
    return (start,end,minValue,maxValue) #Start,End,MinValue to be used for task2/4. MaxValue for task 1. MinValue=MaxValue if both videos have same no. of frames


def main():
    """mat=[[7,2,3],[2,3,4],[4,5,6],[-1,9,4]]
    nr=4
    nc=3
    print greedyMunkres(mat,nr,nc)
    print mat,nr,nc"""
    pass

if __name__ == '__main__':
    main()
