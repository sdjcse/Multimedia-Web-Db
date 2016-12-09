import os
from os.path import dirname

def readFirstThreeCols(infile):
    file = open(infile)
    appendVals = []
    for line in file:
        fields = line.strip().split(';')
        appendVals.append([fields[0],fields[1],fields[2]])
    return appendVals

def getPathToInputVideos(filename):
    currentPath=os.getcwd()
    parent=dirname(currentPath)
    inputVideoPath=os.path.join(parent,"inputVideos",filename)
    return inputVideoPath

def formatOutput(fileToFormat,matrix):
    if fileToFormat == "hist":
        infile = getPathToInputVideos("out_file.chst")
        outfile = getPathToInputVideos("out_file_d.cpca")
    elif fileToFormat == "sift":
        infile = getPathToInputVideos("out_file.sift")
        outfile = getPathToInputVideos("out_file_d.spca")
    elif fileToFormat == "motion":
        infile = getPathToInputVideos("out_file.mvect.filtered")
        outfile = getPathToInputVideos("out_file_d.mpca")
    elif fileToFormat == "kmeansHist":
        infile = getPathToInputVideos("out_file.chst")
        outfile = getPathToInputVideos("out_file_d.ckm")
    elif fileToFormat == "kmeansSift":
        infile = getPathToInputVideos("out_file.sift")
        outfile = getPathToInputVideos("out_file_d.skm")
    elif fileToFormat == "kmeansMotion":
        infile = getPathToInputVideos("out_file.mvect.filtered")
        outfile = getPathToInputVideos("out_file_d.mkm")
    else:
        print("Invalid file to write... Exitnig without writing")
        return None
    appendVals = readFirstThreeCols(infile)
    fOpen = open(outfile,"w")
    for i in range(len(matrix)):
        fOpen.write("%s;%s;%s;"%(appendVals[i][0],appendVals[i][1],appendVals[i][2]))
        for j in range(len(matrix[i])):
            if j!=len(matrix[i])-1:
                fOpen.write("%s,"%matrix[i][j])
            else:
                fOpen.write("%s"%matrix[i][j])
        fOpen.write("\n")
    fOpen.close()

def writeDComp(fileName,matrix):
    fOpen = open(fileName,"w")
    for i in range(matrix.shape[0]):
        indList = list(enumerate(matrix[i]))
        indList.sort(key=lambda tup: tup[1],reverse=True)
        fOpen.write(';'.join('(%s,%s)' % x for x in indList))
        fOpen.write("\n")
    fOpen.close()