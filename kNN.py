from math import sqrt

import numpy as np

def cosine(dataA, dataB):
    if type(dataA) is list and type(dataB) is list:
        if len(dataA) != len(dataB):
            print("Not same length!")
            return -1

        dataLength = len(dataA)
        AB = sum([dataA[i]*dataB[i] for i in range(dataLength)])
        normA = sqrt(sum([i**2 for i in dataA]))
        normB = sqrt(sum([i**2 for i in dataB]))

        denominator = normA * normB
        if denominator == 0:
            return 0
        return AB/denominator
    else:
        print("Input data invalid!")
        return -1

def pearson(dataA, dataB):
    if type(dataA) is list and type(dataB) is list:
        if len(dataA) != len(dataB):
            print("Not same length!")
            return -1

        dataLength = len(dataA)
        #intersection = [i for i in range(dataLength) if dataA[i]!=0 and dataB[i]!=0]
        intersection = [i for i in range(dataLength)]
        if len(intersection) == 0:
            return 0

        #avgA = np.mean([i for i in dataA if i != 0])
        #avgB = np.mean([i for i in dataB if i != 0])
        avgA = np.mean([i for i in dataA])
        avgB = np.mean([i for i in dataB])
        numerator = sum([(dataA[i] - avgA)*(dataB[i] - avgB) for i in intersection])
        deviationA = sqrt(sum([(dataA[i]-avgA)**2 for i in intersection]))
        deviationB = sqrt(sum([(dataB[i]-avgB)**2 for i in intersection]))
        if(deviationA * deviationB)==0:
            return 0
        return numerator/(deviationA*deviationB)


def kNN(data, measure, k = None):
    #simulatedData = [[round(np.corrcoef(i,j)[0,1],3) for j in data] for i in data]
    simulatedData = [[round(measure(i,j),3) for j in data] for i in data]
    newData = []
    for i in range(len(data)):
        newData.append([])
        for j in range(len(data[i])):
            if(data[i][j] == 0):
                userCol = [(simulatedData[i][k], k) for k in range(len(simulatedData[i]))]
                userCol.sort()
                taken = userCol[:k]
                #print(taken)
                #print()
                predictingMean = np.mean([k for k in data[i] if k != 0])
                similarUserMean = [np.mean([l for l in data[k[1]] if l != 0]) for k in taken]
                #print(similarUserMean)
                numerator = sum([simulatedData[i][taken[k][1]]*(data[i][taken[k][1]] - similarUserMean[k]) for k in range(len(taken))])
                denominator = sum([simulatedData[i][taken[k][1]] for k in range(len(taken))])
                #print([simulatedData[i][taken[k][1]] for k in range(len(taken))])
                #print()
                res = predictingMean + numerator/denominator
                newData[i].append(round(res,3))
            else:
                newData[i].append(data[i][j])
    return newData


'''
from scipy import spatial

table2 = [[round(1 - spatial.distance.cosine(i, j),3) for j in data] for i in data]
print()
for i in table2:
    print(i)

table3 = [[round(pearson(i,j),3) for j in data] for i in data]
print()
for i in table3:
    print(i)

table4 = [[np.corrcoef(i,j)[0,1] for j in data] for i in data]
print()
for i in table4:
    print(i)
'''

A = [1,4,5,0,3]
B = [5,1,0,5,2]
C = [4,1,2,5,0]
D = [0,3,4,0,4]

data = [A,B,C,D]

table = [[round(cosine(i,j),3) for j in data] for i in data]
for i in table:
    print(i)

print()
for i in data:
    print(i)
print()
blah = kNN(data, pearson, 2)
for i in blah:
    print(i)
