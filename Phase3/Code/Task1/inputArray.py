import InputParser
import fnmatch
import os


def splitStrToNumList(string):
    return [float(x) for x in string.split(',')]

def getInputsInArrayForm(path,videoNum,component,isAll):
    if component=="hist":
        inputComp = InputParser.getCHist(path)
    elif component=="sift":
        inputComp = InputParser.getSift(path)
    elif component=="motion":
        inputComp=InputParser.getMVect(path)
    else:
        print("No such component")
        return None
    finVid = videoNum
    videoNum = videoNum-1
    parsedArr = []
    if isAll == True:
        #dirpath = "E:\\MWDB\\Phase2\\demoFiles"
        finVid = len(inputComp)#len(fnmatch.filter(os.listdir(dirpath), '*'))
        videoNum = 0

    for videoNum in range(videoNum,finVid):
        numFrames = len(inputComp[videoNum])
        for i in range(numFrames):
            for j in inputComp[videoNum][i]:
                for k in range(len(j)):
                    parsedArr.append([j[k]])
    for i in range(len(parsedArr)):
        parsedArr[i] = splitStrToNumList(parsedArr[i][0])

    return parsedArr
    
def getSiftOfTwoFrames(videoN,fNo):
    inputComp = InputParser.getSift()
    finVid = videoN
    initVid= 0
    parsedArr = []
    workDone = False
    for videoNum in range(initVid,finVid):
        if(videoNum != finVid-1):
            continue
        numFrames = len(inputComp[videoNum])
        for i in range(numFrames):
            if(i != fNo-1):
                continue
            for j in inputComp[videoNum][i]:
                for k in range(len(j)):
                    parsedArr.append([j[k]])
                workDone = True
            if workDone:
                break
        if workDone:
            break
    for i in range(len(parsedArr)):
        parsedArr[i] = splitStrToNumList(parsedArr[i][0])
        
    return parsedArr