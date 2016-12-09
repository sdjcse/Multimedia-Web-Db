import os
from os.path import dirname

def readFirstThreeCols(infile):
    file = open(infile)
    appendVals = []
    for line in file:
        fields = line.strip().split(';')
        inVals = fields[3].split(',')
        appendVals.append([fields[0],fields[1],fields[2],inVals[0],inVals[1]])
    return appendVals

def getPathToInputVideos(filename):
    inputVideoPath=os.path.join(os.pardir,"iofiles",filename)
    return inputVideoPath

def formatOutput(fileToFormat,matrix,path):
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
    appendVals = readFirstThreeCols(path)
    fOpen = open(outfile,"w")
    for i in range(len(matrix)):
        fOpen.write("%s;%s;%s;%s,%s,"%(appendVals[i][0],appendVals[i][1],appendVals[i][2],appendVals[i][3],appendVals[i][4]))
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