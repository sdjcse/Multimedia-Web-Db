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
import sys,videoComparer,InputParser
from distancemeasure import distanceMeasures
import timeit

featuresList=["Color Histogram","Sift","Motion Vectors"]
MetricsList=["L1 Distance","Cosine Similarity","Mahalanobis Distance","Intersection Similarity","Euclidean Distance","L-Infinity Distance","Intersection Similarity M2"]

def dummyVideoComparer(feature,metric,Vi,Vj):
    featureMatrix=None
    if feature==featuresList[0]:
        featureMatrix=InputParser.getCHist()
    elif feature==featuresList[1]:
        featureMatrix=InputParser.getSift()
    elif feature==featuresList[2]:
        featureMatrix=InputParser.getMVect()

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
    distVal=videoComparer.compareVideos(featureMatrix[Vi],0,len(featureMatrix[Vi])-1,featureMatrix[Vj],0,len(featureMatrix[Vj])-1,metricFuntion,metric,1)
    return distVal


def main():
    if len(sys.argv)<>4:
        print "Usage: python task1.py subtaskID Vi Vj"
        quit()
    subtaskID=sys.argv[1]
    Vi=int(sys.argv[2])
    Vj=int(sys.argv[3])
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
            feature=featuresList[2]#MVect
            if subtaskID[1]=='e':
                metric=MetricsList[0] #L1 Distance
            else:
                metric=MetricsList[1] #Cosine Similarity

        overallValue=dummyVideoComparer(feature,metric,Vi,Vj)
        print metric+"="+str(overallValue)

    else:
        if subtaskID[1]=='g':
            metric=MetricsList[3] #Intersection Similarity
        else:
            metric=MetricsList[0] #L1 Distance
        overallValue=0
        for i in range(0,len(featuresList)):
            distVal=dummyVideoComparer(featuresList[i],metric,Vi,Vj)
            if "Similarity" in metric: #To check if it is a similarity measure
                if distVal==0.0:
                    distVal=sys.maxsize #Some huge value to avoid division by zero
                else:
                    distVal=float(1/distVal) -1 #Convert similarity to distance
                    distVal=abs(distVal) #Just in case
            overallValue+=distVal
        if "Similarity" in metric:
            overallValue=1/(1+overallValue)
        print metric+"="+str(overallValue)


if __name__ == '__main__':
    #print "Started"
    startM=timeit.default_timer()
    main()
    endM=timeit.default_timer()
    print "Time Taken for execution:"+str(endM-startM)+" seconds"

