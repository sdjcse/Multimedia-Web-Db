# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 03:48:25 2016

@author: Uthara
"""

import numpy as np
import sys
import glob
sys.path.append("E:\MWDB\phase3\output")
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
	#openFile = open("E:\MWDB\phase3\iofiles\graphdata_d_k.gspc")
	#openFile = open("E:\MWDB\phase3\iofiles\dummy.txt")
	# numVids,numFrames = numVidsnumFrames("directory")
	inputGraph=input("Enter the path of the graph file : ")
	openFile = open(inputGraph)
	numVids = 10
	numFrames = 75

	prod = FrameCounter.countFramesInFolder(vidPath)
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

'''
Computes Q values as in ASCOS++ paper

Q = pij(1-exp(-aij))

aij = adjacency matrix weight values
pij = normalized adjacency values

'''
    
def qVal(simMat,normMat):
	negOne = np.array([-1])
	posOne = np.array([1])
	negatedSim = np.multiply(simMat,negOne)
	negatedSim = np.exp(negatedSim)
	negatedSim = np.multiply(simMat,negOne)
	negatedSim = np.add(simMat,posOne)
	qVal = np.multiply(negatedSim,normMat)
	return qVal
            
'''
uses the above qVal function to compute similarity

S = Inverse of (1-c*Transpose(Q)) * (1-c) I
sums over the s column wise to find 

yet to decide on relative factor c
c is the relative factor it decides the relation between direct neighbours
and indirect neighbours lower the value less important the indirect neighbours are

'''
def ascosplus():
	vidPath = input("Please enter video DB Path: ")
	vidPathWoStar = vidPath
	vidPath += '\*'
	topD = input("Please enter top-D ranking frames to show: ")
	c = 0.6
	mainDict,similarityMatrix = readFile(vidPathWoStar)
	normalizedSim = similarityMatrix / np.sum(similarityMatrix,axis=0)
	np.nan_to_num(normalizedSim)
	where_are_NaNs = np.isnan(normalizedSim)
	normalizedSim[where_are_NaNs] = 0
	qMat = qVal(similarityMatrix,normalizedSim)

	print("Enter the 3 seed frames: Video number followed by Frame number")
	significantFrames = []
	seedSize = np.shape(normalizedSim)[0]	# seedSize is the length of input

	for i in range(3):
		vid = input("Enter the video number: ")
		frame = input("Enter the frame number: ")
		t = (int(vid), int(frame))
		significantFrames.append(t)

	ident = np.identity(qMat.shape[0])
	alpha = 0.85
	weight = np.zeros(ident.shape)

	for vi in significantFrames:
		weight[:,mainDict[vi]] = 1.0/3.0

	weightedQMat = alpha*qMat.transpose() + (1-alpha)*weight
	matToInv = np.subtract(ident,c*weightedQMat)
	finalSim = np.dot(np.linalg.inv(matToInv),(1-c)*ident)
	sumOverColums = finalSim.sum(axis=0)
	numNodes = finalSim.shape[0]
	sumOverColums = np.divide(sumOverColums,np.array(numNodes))
	
	
	idx = sumOverColums.argsort()[::-1]
	for i in range(0,int(topD)):
		var = (list(mainDict.keys())[list(mainDict.values()).index(idx[i])])
		print('{} - {}'.format(var,sumOverColums[idx[i]]))
		DisplayFrame.displayFrame(glob.glob(vidPath)[var[0]],var[1])

ascosplus()