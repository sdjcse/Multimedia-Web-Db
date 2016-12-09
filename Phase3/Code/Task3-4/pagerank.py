# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:55:09 2016

@author: Dhananjayan
"""
import numpy as np
import sys
import glob
import operator
#sys.path.append("E:\MWDB\phase3\output")
import FrameCounter
import DisplayFrame


'''
Assuming that the input file is in the following format

vidNum,FrameNum,vidNum,frameNum,similarity

'''

'''
Function to make entry into the dictionary
'''
def makeNewEntry(mainDict,var1,var2):
    counter = len(mainDict)
    tupleToIns = (int(var1),int(var2))
    if tupleToIns not in mainDict:
        mainDict[tupleToIns] = counter
        counter +=1
    return tupleToIns

'''
Function to be written once input files are given 
reads the number of videos from a directory and number of frames in each video
in total
'''
def numVidsnumFrames(dir):
    numVids = 0
    numFrames = 0
    return numVids,numFrames

'''
This function will read the values from file and maps it into array
each vidNum,FrameNum tuple is mapped to a index which is used to refer
matrices

> Creates an n*n matrix as n = numVids * numFrames
> maps the similarity values column-wise
> returns the mapping dictionary and matrix
'''    
def readFile(vidPath):
    tupleToInxMapper = dict()
    inputGraph=input("Enter the path of the graph file : ")
    openFile = open(inputGraph)
    numVids = 10
    numFrames = 75
    prod = FrameCounter.countFramesInFolder(vidPath)
    #print(prod)
    #prod = numVids*numFrames
    similarityMatrix = np.zeros((prod,prod))
    for line in openFile:
        line=line.replace("<","")
        line=line.replace(">","")
        arr = line.split(",")
        tup1 = makeNewEntry(tupleToInxMapper,arr[0],arr[1])
        tup2 = makeNewEntry(tupleToInxMapper,arr[2],arr[3])
        similarity = float(arr[4])
        similarityMatrix[tupleToInxMapper[tup2]][tupleToInxMapper[tup1]] = similarity
    return tupleToInxMapper,similarityMatrix
    
def computePR(p, s, normalizedSim):
    #print(type(p))
    #print(type(normalizedSim))
    alpha = 0.01
    converge = 0.0001
    for i in range(1000):
        p2 = np.copy(p)
        p = alpha*(normalizedSim.dot(p2)) + (1-alpha)*s
        d = p - p2
        diff = 0.0
        for i in range(len(d)):
            diff = d[i]*d[i]
        diff = np.sum(diff,axis=0)
        diff = diff**0.5
        if diff<converge:
            break
    return p
'''
This function computes page rank on the given matrix

> the given similarity matrix is used to find the eigen values and eigen vectors
> After that the vectors are sorted and the corresponding indices are
outputted with the mapping vidNum FrameNum tuple in the dictionary
'''
def pageRank():
    vidPath = input("Please enter video DB Path with trailing slash: ")
    vidPathWoStar = vidPath
    vidPath += '*'
    topD = input("Please enter top-D ranking frames to show: ")
    mainDict,similarityMatrix = readFile(vidPathWoStar)
    normalizedSim = similarityMatrix / np.sum(similarityMatrix,axis=0)
    
    np.nan_to_num(normalizedSim)
    where_are_NaNs = np.isnan(normalizedSim)
    normalizedSim[where_are_NaNs] = 0
    p = []
    #print(normalizedSim)
    seedSize = np.shape(normalizedSim)[0]
    for i in range(seedSize):
        p.append(1.0/float(seedSize))
    p = np.transpose(np.array(p))
	#s = np.transpose(np.array(s))
    p = computePR(p,p, normalizedSim)
    idx = p.argsort()[::-1]
    p = p[idx]
    #np.set_printoptions(threshold=np.nan)
    #print(p)
    counter = 0
    for i in range(0,int(topD)):
        #print(i)
        #print(idx[i])
        var = (list(mainDict.keys())[list(mainDict.values()).index(idx[i])])
        print('{} - {}'.format(var,p[i]))
        DisplayFrame.displayFrame(glob.glob(vidPath)[var[0]],var[1])
        counter += 1
    print(counter)

def personalizedPageRank_RPR2():
    vidPath = input("Please enter video DB Path with trailing slash: ")
    vidPathWoStar = vidPath
    vidPath += '*'
    topD = input("Please enter top-D ranking frames to show: ")
    mainDict,similarityMatrix = readFile(vidPathWoStar)
    normalizedSim = similarityMatrix / np.sum(similarityMatrix,axis=0)
        
    np.nan_to_num(normalizedSim)
    where_are_NaNs = np.isnan(normalizedSim)
    normalizedSim[where_are_NaNs] = 0
    print("Enter the 3 seed frames: Video number followed by Frame number")
    significantFrames = []
    seedSize = np.shape(normalizedSim)[0]

    for i in range(3):
        vid = input("Enter the video number: ")
        frame = input("Enter the frame number: ")
        t = (int(vid), int(frame))
        significantFrames.append(t)
    p = []
    for i in range(seedSize):
        p.append(1.0/float(seedSize))	
	
	#Finding seed vector
    
    #s = []
    s = np.zeros(seedSize)
    for i in significantFrames:
        s[mainDict[i]] = 1.0 / 3.0

    p = np.transpose(np.array(p))
    s = np.transpose(s)	
    ppr = computePR(p,s,normalizedSim)
 
	#RPR-2
    pi_vi = dict() #*****the pi function in step1
    sum_vi = dict() #*****the summation in step2
    #Step 1
    for vi in significantFrames:
        # seedSize is the length of input 
        s = np.zeros(seedSize)
        s[mainDict[vi]] = 1.0
        s = np.transpose(s)
        pi_vi[vi] = computePR(p,s,normalizedSim)
    
    #Step 2
    for vi in significantFrames:
        sum_vi[vi] = 0
        for vj in significantFrames:
            sum_vi[vi] += pi_vi[vi][mainDict[vj]]
    
    critVal = sum_vi[max(sum_vi.items(), key=operator.itemgetter(1))[0]]
    S_crit = []
    for key in sum_vi.keys():
        if critVal - sum_vi[key] < 0.00001:
            S_crit.append(key)						 #*****Step 3******
    rpr2 = np.zeros(seedSize)
    print(S_crit)
    for vi in S_crit:
        rpr2 = np.add(rpr2, pi_vi[vi])
    rpr2 = rpr2/len(S_crit)             			 #*****Step 4******
    
	#*****************************************************************
    
    idx = rpr2.argsort()[::-1]
    rpr2 = rpr2[idx]
    counter = 0
    for i in range(0,int(topD)):
        #print(i)
        var = (list(mainDict.keys())[list(mainDict.values()).index(idx[i])])
        print('{} - {}'.format(var,rpr2[i]))
        DisplayFrame.displayFrame(glob.glob(vidPath)[var[0]],var[1])
        counter += 1
    print(counter)
pro = input("What you want to run(Enter 1 or 2)? 1.PageRank or 2.RPR : ")
if(pro=='1'):
    pageRank()
elif(pro=='2'):
    personalizedPageRank_RPR2()
