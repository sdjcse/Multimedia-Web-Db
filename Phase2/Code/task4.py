#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     09/10/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys,videoComparer,InputParser,DisplayVideo
## videoComparer.py to compare two videos; distanceMeasures.py contains all the functions to calculate distances/similarity; inputVectors.py to get the phase 1 input in a matrix form; DisplayVideo.py to play the video clip;
import os,operator
from distancemeasure import distanceMeasures
import timeit

featuresList=["Color Histogram","Sift","Motion Vectors"]
MetricsList=["L1 Distance","Cosine Similarity","Mahalanobis Distance","Intersection Similarity","Euclidean Distance","L-Infinity Distance","Intersection Similarity M2"]

def dummyVideoComparer(feature,metric,Vi,frameStartA,frameEndB,Vj):
    featureMatrix=None
    if feature==featuresList[0]:
        featureMatrix=InputParser.getCHistPCA()#PCA
        #featureMatrix=InputParser.getCHistKM() #K Means
    elif feature==featuresList[1]:
        featureMatrix=InputParser.getSiftPCA()#PCA
        #featureMatrix=InputParser.getSiftKM()#K Means
    elif feature==featuresList[2]:
        featureMatrix=InputParser.getMVectPCA() #PCA
        #featureMatrix=InputParser.getMVectKM() #KM

    metricFuntion=None
    dm=distanceMeasures(featureMatrix,metric)
    #Change according to the distanceMeasures.py file
    if metric==MetricsList[0]:
        metricFuntion=dm.l1Distance
    elif metric==MetricsList[1]:
        metricFuntion=dm.cosineSimilarity
    elif metric==MetricsList[2]:
        metricFuntion=dm.MahalanobisDistance
    elif metric==MetricsList[3]:
        metricFuntion=dm.intersectionSimilarity
    elif metric==MetricsList[4]:
        metricFuntion=dm.l2Distance
    elif metric==MetricsList[6]:
        metricFuntion=dm.intersectionSimilarityM2
    #Add more if needed

    #To take care of edge cases pertaining to frame range given
    difference=frameEndB-frameStartA

    if frameEndB>len(featureMatrix[Vi])-1:
        frameEndB=len(featureMatrix[Vi])-1

    if frameStartA>len(featureMatrix[Vi])-1:
        frameStartA-=len(featureMatrix[Vi])-1-difference
    if frameStartA<0:
        frameStartA=0

    (start,end,distVal,maxVal)=videoComparer.compareVideos(featureMatrix[Vi],frameStartA,frameEndB,featureMatrix[Vj],0,len(featureMatrix[Vj])-1,metricFuntion,metric,2)
    return (start,end,distVal,maxVal)


def main():
    if len(sys.argv)<>7:
        print "Usage: python task4.py subTaskID Vi a b dirPath k"
        quit()
    subtaskID=sys.argv[1]
    Vi=int(sys.argv[2]) #Video i of which frames [a,b] are to be compared
    frameStartA=int(sys.argv[3])
    frameEndB=int(sys.argv[4])
    videoDirectoryPath=sys.argv[5]
    kValue=int(sys.argv[6])
    videoList=os.listdir(videoDirectoryPath)
    distanceValueDict={}
    #Vj=int(sys.argv[3])
##Vi,Vj being the two videos to be compared. Sub Task ID is one of the 8 tasks under task 1
    feature=''
    metric=''
    if subtaskID!='1g' and subtaskID!='1h':
        if subtaskID=='1a' or subtaskID=='1b':
            feature=featuresList[0] #Color Histogram"
            if subtaskID[1]=='a':
                metric=MetricsList[3] #Intersection Similarity
            else:
                metric=MetricsList[1] #Cosine Similarity

        elif subtaskID=='1c' or subtaskID=='1d':
            feature=featuresList[1] #Sift
            if subtaskID[1]=='c':
                metric=MetricsList[6] #Intersection Similarity M2
            else:
                metric=MetricsList[2] #Mahalanobis Distance

        elif subtaskID=='1e' or subtaskID=='1f':
            feature=featuresList[2]
            if subtaskID[1]=='e':
                metric=MetricsList[0] #L1 Distance
            else:
                metric=MetricsList[1] #Cosine Similarity
        for Vj in range(0,len(videoList)):
            (start,end,overallValue,maxDist)=dummyVideoComparer(feature,metric,Vi,frameStartA,frameEndB,Vj)
            distanceValueDict[Vj]=[overallValue,start,end]
            #print overallValue

    else:
        if subtaskID[1]=='g':
            metric=MetricsList[3] #Intersection SImilarity
        else:
            metric=MetricsList[0] #L1 Distance
        for Vj in range(0,len(videoList)):
            overallValue=0.0
            for i in range(0,len(featuresList)):
                (start,end,distVal,maxDist)=dummyVideoComparer(featuresList[i],metric,Vi,frameStartA,frameEndB,Vj)
                if "Similarity" in metric: #To check if it is a similarity measure
                    if distVal==0.0:
                        distVal=sys.maxsize #Some huge value to avoid division by zero
                    else:
                        distVal=float(1/distVal)-1 #Convert similarity to distance
                        distVal=abs(distVal)
                overallValue+=distVal
            distanceValueDict[Vj]=[overallValue,start,end]
            #print overallValue

    #Negate similarity so as to sort it in descending order of similarity
    if "Similarity" in metric:
        for key in distanceValueDict.keys():
            distanceValueDict[key][0]*=-1

    sortedDistanceValues=sorted(distanceValueDict.items(),key=lambda Dist:Dist[1][0]) #Sort based on Distance values
    counter=-1
    #print sortedDistanceValues

    #Play the Query
    name=videoList[Vi]
    fullPath=os.path.join(videoDirectoryPath,name)
    print "Query: "+fullPath,frameStartA,frameEndB
    print "\n"
    DisplayVideo.outputProcessor(fullPath,frameStartA,frameEndB) #Play the video given Path,Start and End Frames

    print "Top "+str(kValue)+" most similar sequences are:"
    for videoNo,distanceFrames in sortedDistanceValues:
        counter+=1
        if counter>=kValue: #Play top 'k' sequences 1 from each video in the directory
            break
        name=videoList[videoNo]
        fullPath=os.path.join(videoDirectoryPath,name)
        print fullPath,distanceFrames[1],distanceFrames[2]
        DisplayVideo.outputProcessor(fullPath,distanceFrames[1],distanceFrames[2]) #Play the video given Path,Start and End Frames




if __name__ == '__main__':
    start=timeit.default_timer()
    main()
    end=timeit.default_timer()
    print "Time Taken for execution:"+str(end-start)+" seconds"

