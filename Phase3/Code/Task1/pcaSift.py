# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:54:33 2016

@author: Dhananjayan
"""

import numpy as np
import inputArray
import outputWriter

def pcaSift():
    path = input('Enter the path of file to read: ')
    inputArr = inputArray.getInputsInArrayForm(path,0,"sift",True)
    compList = np.asarray(inputArr)
    # row - data
    # colum - variable    
    compList = np.delete(compList,np.s_[0:2],axis=1)
    print(compList.shape)
    findCov = np.array(inputArr)
    findCov = np.delete(findCov,np.s_[0:2],axis=1)
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
    outputWriter.formatOutput("sift",outputArr,path)
    #outputWriter.writeDComp("siftDComp.spca",extracted)
    print("Reduced dimension size: ",outputArr.shape)
    print("Wrote output into the file..")

pcaSift()