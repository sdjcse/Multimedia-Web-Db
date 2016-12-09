import sys
#sys.path.insert(1,'E:\\MWDB\\Phase2\\code\\mainSource\\phasetwo\\pca')
from sklearn.cluster import KMeans
import numpy
import inputArray
import outputWriter

def kmeansMotion():
    print("Enter the number of dimensions ")
    d = int(input())
    motionArray = inputArray.getInputsInArrayForm(0,"motion",True);
    kmeans = KMeans(n_clusters=d, random_state=0).fit(motionArray)
    clusterArray = kmeans.cluster_centers_
    reducedVectors = []
    for i in range(len(motionArray)):
        newVector = []
        for j in range(d):
            p = numpy.dot(motionArray[i], clusterArray[j])
            newVector.append(p)
        reducedVectors.append(newVector)
    outputWriter.writeDComp("mvectDComp.mkmeans",clusterArray)
    print("Output vector generated of dimension:")
    print(len(reducedVectors),len(reducedVectors[0]))
    outputWriter.formatOutput("kmeansMotion", reducedVectors)

kmeansMotion()