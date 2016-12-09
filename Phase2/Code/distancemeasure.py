import numpy as np

def splitStrToNumList(string):
    return [float(x) for x in string.split(',')]

def calculateInverse(inputComp):
    finVid=len(inputComp)
    parsedArr = []
    for videoNum in range(0,finVid):
        numFrames = len(inputComp[videoNum])
        for i in range(numFrames):
            for j in inputComp[videoNum][i]:
                for k in range(len(j)):
                    parsedArr.append([j[k]])
    for i in range(len(parsedArr)):
        parsedArr[i] = parsedArr[i][0] #splitStrToNumList(parsedArr[i][0])

    parsedArrToNPArr=np.array(parsedArr)
    covariance=np.cov(parsedArrToNPArr,None,False,False,0)
    #print covariance
    S=np.linalg.pinv(covariance)
    return S

class distanceMeasures:
    def __init__(self,data,metric):
        if metric=="Mahalanobis Distance":
            self.Sinv=calculateInverse(data)
        else:
            self.Sinv=None

    def MahalanobisDistance(self,v1,v2):
        v1Arr=np.array(v1)
        v2Arr=np.array(v2)
        diff=v1Arr-v2Arr
        S=np.array(self.Sinv)
        v1S=np.dot(diff,S)
        dist=np.dot(v1S,diff)
        #print dist
        return dist**0.5

    def l1Distance(self,v1, v2):
        dist = 0.0
        for i in range(len(v1)):
            dist += abs((v1[i]) - (v2[i]))
        #print dist
        return dist

    def l2Distance(self,v1, v2):
        dist = 0.0
        for i in range(len(v1)):
            dist += (v1[i] - v2[i]) ** 2
        dist = dist ** 0.5
        #print dist
        return dist

    def linfDistance(self,v1, v2):
        dist = 0.0
        for i in range(len(v1)):
            if abs(v1[i]-v2[i]) > dist:
				dist = abs(v1[i]-v2[i])
        #print dist
        return dist

    def cosineSimilarity(self,v1, v2):
        dist = np.dot(v1, v2)
        norm_v1 = 0.0
        norm_v2 = 0.0
        for i in range(len(v1)):
            #dist+=v1[i]*v2[i] #Over dot
            norm_v1 += v1[i] ** 2
            norm_v2 += v2[i] ** 2
        dist = dist/((norm_v1 ** 0.5) * (norm_v2 ** 0.5))
        #print dist
        return dist

    def intersectionSimilarity(self,v1, v2):
        minSum = 0.0
        maxSum = 0.0
        for i in range(len(v1)):
            minSum += min(abs(v1[i]), abs(v2[i]))
            maxSum += max(abs(v1[i]), abs(v2[i]))
        dist = minSum/maxSum
        #print dist
        return dist

    def intersectionSimilarityM2(self,v1,v2):
        totalSum=0.0
        for i in range(0,len(v1)):
            if v1[i]!=0.0 and v2[i]!=0.0:
                dr=max(abs(v1[i]),abs(v2[i]))
                nr=min(abs(v1[i]),abs(v2[i]))
                totalSum+=nr/dr
        return totalSum/len(v1)




#l1Distance([1,2,3], [4.5,5.5,6.5])
#l2Distance([1,2,3], [4.5,5.5,6.5])
#linfDistance([1,2,3], [4.5,5.5,6.5])
#cosineSimilarity([1,2,3], [4.5,5.5,6.5])
#intersectionSimilarity([1,2,3], [4.5,5.5,6.5])