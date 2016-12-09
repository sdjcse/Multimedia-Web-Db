# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:54:33 2016

@author: Dhananjayan
"""

import numpy as np
import inputArray
import outputWriter

def pcaMotion():
    inputArr = inputArray.getInputsInArrayForm(0,"motion",True)
    compList = np.asarray(inputArr)
    # row - data
    # colum - variable    
    findCov = np.array(inputArr)
    covMat = np.cov(findCov,None,False,False,0)
    
    w = np.linalg.eigh(covMat)[0]
    v = np.linalg.eigh(covMat)[1]
    
    idx = w.argsort()[::-1]
    w = w[idx]
    w = np.diag(w)
    v = v[:,idx]
    
    reduceToD = input("Enter the D value to reduce the dimensions: ")
    
    extracted = v[:,:int(reduceToD)]
    extracted = extracted.T
    outputArr = np.dot(extracted,compList.T)
    
    outputArr = outputArr.T
    
    outputWriter.formatOutput("motion",outputArr)
    outputWriter.writeDComp("motionDComp.mpca",extracted)
    print("Reduced dimension size: ",outputArr.shape)
    print("Wrote output into the file..")

pcaMotion()