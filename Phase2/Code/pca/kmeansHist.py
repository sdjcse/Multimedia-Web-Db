import sys
#sys.path.insert(1,'E:\\MWDB\\Phase2\\code\\mainSource\\phasetwo\\pca')
from sklearn.cluster import KMeans
import numpy
import inputArray
import outputWriter

def kmeansHist():
    print("Enter the number of dimensions ")
    d = int(input())
    histArray = inputArray.getInputsInArrayForm(0,"hist",True);
    kmeans = KMeans(n_clusters=d, random_state=0).fit(histArray)
    clusterArray = kmeans.cluster_centers_
    reducedVectors = []
    for i in range(len(histArray)):
        newVector = []
        for j in range(d):
            p = numpy.dot(histArray[i], clusterArray[j])
            newVector.append(p)
        reducedVectors.append(newVector)
    outputWriter.writeDComp("histDComp.hkmeans",clusterArray)
    print("Output vector generated of dimension:")
    print(len(reducedVectors),len(reducedVectors[0]))
    outputWriter.formatOutput("kmeansHist", reducedVectors)

kmeansHist()