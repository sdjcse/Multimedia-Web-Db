# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:07:27 2016

@author: Darshan Shetty

Main Script to perform Task 2 operations
Parse the input from Task 1 and use it to obtain similarity measure for frames
in the video based on SIFT vector
"""
import copy
import sys
import os
import InputParser
from sklearn.neighbors import NearestNeighbors

def cleanUp(filePath):
    try:
        os.remove(filePath)
    except OSError:
        pass

def main():
    if len(sys.argv) != 3:
        print("Usage: python task2.py k path")
        quit()
    k=int(sys.argv[1])
    fileLocation=sys.argv[2]
    outFileName='filename_d_k_10.gspc'
    outFolderPath=os.path.dirname(os.path.abspath(fileLocation))
    outFilePath=os.path.join(outFolderPath,outFileName)
    cleanUp(outFilePath)
    fileOut=open(outFilePath,"w")
    featureMatrix=InputParser.getSift(fileLocation)
    #Use this to ensure that original data is not manipulated during distance
    #calcution
    matrixCp=copy.deepcopy(featureMatrix)
    for video in matrixCp:
        for frame in video:
            for vector in frame:
                vector=vector[2:]
    #For each frame in the video determine the best fit consdering frames from other videos
    for videoIndex in range(len(matrixCp)):
        for frameIndex in range(len(matrixCp[videoIndex])):
            #print("Staring for video ",videoIndex, " frame ",frameIndex)
            frameVectors=matrixCp[videoIndex][frameIndex]
            originalVectors=featureMatrix[videoIndex][frameIndex]
            searchTemplate = NearestNeighbors(n_neighbors=1,metric='manhattan',n_jobs=-1)
            searchTemplate.fit(frameVectors)
            frameDistanceList=[]
            for vidIndex in range(videoIndex+1,len(matrixCp)):
                for frIndex in range(len(matrixCp[vidIndex])):
                    searchCandidate=matrixCp[vidIndex][frIndex]
                    #print("Comparing with video ",vidIndex, " frame ",frIndex)
                    distances, indices = searchTemplate.kneighbors(searchCandidate)
                    frameDist=0.0
                    for index in range(len(searchCandidate)):
                        searchSift=searchCandidate[index]
                        origSift=originalVectors[indices[index][0]]
                        #print(searchSift)
                        #print(origSift)
                        searchDist=distances[index][0]
                        #searchDist1=distances[index][1]
                        #if searchDist!=0 and searchDist1!=0 :
                        #    if searchDist/searchDist1>1.0 or searchDist1/searchDist>1.0:
                                #print("Search Distance: ",searchDist)
                        locDist=(((searchSift[0]-origSift[0])**2) +((searchSift[1]-origSift[1])**2))**0.5
                                #More weightage given for location over other descriptors
                        vectDist=0.7*locDist+0.3*searchDist
                        frameDist+=vectDist
                    #print("Frame Distance between video ",videoIndex+1," frame "frameIndex+1,frameDist)
                    frameDistanceList.append([vidIndex,frIndex,frameDist])
            print(frameDistanceList)
            frameDistanceList.sort(key=lambda litem: (litem[2],litem[0]))
            #sorted(frameDistanceList, key=itemgetter(2))
            print(frameDistanceList)
            requiredList=frameDistanceList[:k]
            #Write data to file now
            for data in requiredList:
                sourceFrame="<"+str(videoIndex+1)+","+str(frameIndex+1)+">"+","
                simFrame="<"+str(data[0]+1)+","+str(data[1]+1)+">"+","
                distance=data[2]
                sim=1/(1+distance)
                line=sourceFrame+simFrame+str(sim)
                print(line)
                fileOut.write(line)
                fileOut.write("\n")
    fileOut.close();
    
if __name__ == '__main__':
    main()