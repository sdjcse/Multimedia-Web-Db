import sys,math,os,random,timeit
import numpy as np
from optparse import OptionParser

class LSHFamily:
    def __init__(self,data,useMahalanobisDist,noOfLayersL,noOfBucketsPerLayer,noOfDimensions,gridsize,modvalue):
        self.data=data
        self.Sinv=None
        if (useMahalanobisDist):
            self.Sinv=self.findSinv()
        self.width=modvalue
        self.gridsize=gridsize
        self.noOfLayers=noOfLayersL
        self.noOfBucketsPerLayer=noOfBucketsPerLayer
        self.noOfDimensions=noOfDimensions
        noOfHashFunctionsPerLayer_f=math.ceil(self.noOfBucketsPerLayer/float(modvalue))
        self.noOfHashFunctionsPerLayer=int(noOfHashFunctionsPerLayer_f)
        #print self.noOfHashFunctionsPerLayer
        self.randomUnitVectors=[]

    def findSinv(self):
        siftVrmatrix=[]
        for each in self.data:
            siftVrmatrix.append(each[1])
        siftVrmatrix_NpArray=np.array(siftVrmatrix)
        covarainceMatrix=np.cov(siftVrmatrix_NpArray,None,False,False,0)
        Sinv=np.linalg.pinv(covarainceMatrix)
        return Sinv

    def normalizeVector(self,vector):
        length=0.0
        for i in range(0,len(vector)):
            length+=vector[i]**2
        length=length**0.5
        unitVector=[]
        for i in range(0,len(vector)):
            unitVector.append(float(vector[i]/length))
        return unitVector

    def generateRandomUnitVectors(self):
        randomDistVal=5
        for i in range(0,self.noOfLayers):
            for j in range(0,self.noOfHashFunctionsPerLayer):
                randomVector=random.sample(range(-randomDistVal*self.noOfDimensions,randomDistVal*self.noOfDimensions),self.noOfDimensions)
                unitRandomVr=self.normalizeVector(randomVector)
                self.randomUnitVectors.append(unitRandomVr)
        #print ("Length of hash unit vrs",len(self.randomUnitVectors))

    def findProjections(self,vector):
        bucketID=''
        for i in range(0,self.noOfLayers):
            tempBucketID=''
            for j in range(0,self.noOfHashFunctionsPerLayer):
                eachUnitVector=self.randomUnitVectors[i*self.noOfHashFunctionsPerLayer+j]
                projection=0.0
                if self.Sinv!=None:
                    projection=np.dot(np.dot(vector,self.Sinv),eachUnitVector)#Mahalanobis
                else:
                    projection=np.dot(vector,eachUnitVector) #Euclidean Distance
                projection/=self.gridsize
                hashProjectionGrid=math.floor(projection)%(2**self.width) #010 - width=3
                gridVal=str(bin(int(hashProjectionGrid)))[2:]
                append=self.width-len(gridVal)
                tempBucketID+='0'*append+gridVal
            bucketID+=tempBucketID[:self.noOfBucketsPerLayer]
        return bucketID

def concat(a,b):
    return str(a)+","+str(b)

def parsePCASiftFile(path):
    f=open(path,"r")
    lines=f.readlines()
    retListOfTuples=[]
    for line in lines:
        line=line[:len(line)-1]
        var=""
        tokens=line.split(",") #SIFT input file of the form vidNo;FrameNo;CellNo;x,y,ReducedDims
        var=tokens[0]+";"+tokens[1]#So tokens[0] will have vidNo;FrameNo;CellNo;x and tokens[1] will have y
        dims=[float(t) for t in tokens[2:]]#tokens[2:] #2 to len of the tokens will have the reduced dimensions
        retListOfTuples.append((var,dims))
    f.close()
    return retListOfTuples

def performLSH(data,noOfLayers,noOfBuckets,useMahalanobis,gridSize,width):
    outputFileData=[]
    K=int(math.log(noOfBuckets,2))
    hashTableSet=[]
    for l in range(0,noOfLayers):
        hashTableSet.append([])
        for k in range(0,noOfBuckets):
            hashTableSet[l].append([])
    dimensions=len(data[0][1])
    lsh=LSHFamily(data,useMahalanobis,noOfLayers,K,dimensions,gridSize,width)
    lsh.generateRandomUnitVectors()
    count=0
    for siftVector in data:
        bucketIDs=lsh.findProjections(siftVector[1])
        count+=1
        for i in range(0,noOfLayers):
            eachLayerBucket=int(bucketIDs[int(i*K):int((i+1)*K)],2)
            hashTableSet[i][eachLayerBucket].append(siftVector[0])
            layerAndBucketNo=concat(i,eachLayerBucket)+","
            lineToBeWritten=layerAndBucketNo+"<"+siftVector[0]+">\n"
            outputFileData.append(lineToBeWritten)
    return (hashTableSet,outputFileData)

def main():
    parser=OptionParser()
    parser.add_option("-I",action="store",type="string",dest="inFilePath",default="out_file_d.spca",help="Input file name of the form filename_d.spca, default name out_file_d.spca")
    parser.add_option("-L",action="store",type="int",dest="noOfLayersL",default=3,help="Number of layers L, default value=3")
    parser.add_option("-K",action="store",type="int",dest="noOfBits",default=15,help="Number of buckets per layer, 2^K, default value=15")
    parser.add_option("-O",action="store",type="string",dest="outFilePath",default="out_file_d.lsh",help="Output File of the form filename_d.lsh, default name of the form InputFileName_d.lsh")
    parser.add_option("-D",action="store",type="float",dest="gridSize",default=0.12,help="Size of each grid D, default value=0.12")
    parser.add_option("-M",action="store_false",dest="useMahalanobis",default=False,help="Define whether to use Mahalanobis Distance over Euclidean, The option is Disabled")
    parser.add_option("-b",action="store",dest="band",type="int",default=2,help="No. of Bits each hash function contributes, Default value=2")
    (options,args)=parser.parse_args(sys.argv)
    data=parsePCASiftFile(options.inFilePath)
    noOfBuckets=2**options.noOfBits
    (lshtable,outputFileData)=performLSH(data,options.noOfLayersL,noOfBuckets,options.useMahalanobis,options.gridSize,options.band)
    #print("Writing to file...")
    fout=open(options.outFilePath,"w")
    for eachLine in outputFileData:
        fout.write(eachLine)
    fout.close()
    return

if __name__ == '__main__':
    startM=timeit.default_timer()
    main()
    endM=timeit.default_timer()
    print ("Time Taken for execution:"+str(endM-startM)+" seconds")
