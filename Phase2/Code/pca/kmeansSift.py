import sys
#sys.path.insert(1,'E:\\MWDB\\Phase2\\code\\mainSource\\phasetwo\\pca')
from sklearn.cluster import KMeans
import numpy
import inputArray
import outputWriter

def kmeansSift():
    print("Enter the number of dimensions ")
    d = int(input())
    siftArray = inputArray.getInputsInArrayForm(0,"sift",True);
    kmeans = KMeans(n_clusters=d, random_state=0).fit(siftArray)
    clusterArray = kmeans.cluster_centers_
    reducedVectors = []
    for i in range(len(siftArray)):
        newVector = []
        for j in range(d):
            p = numpy.dot(siftArray[i], clusterArray[j])
            newVector.append(p)
        reducedVectors.append(newVector)
    outputWriter.writeDComp("siftDComp.skmeans",clusterArray)
    print("Output vector generated of dimension:")
    print(len(reducedVectors),len(reducedVectors[0]))
    outputWriter.formatOutput("kmeansSift", reducedVectors)

kmeansSift()