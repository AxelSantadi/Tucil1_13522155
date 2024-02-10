import numpy as np
import random

def makeMatrix(jumlahToken, listTokenFinal, x, y):
    matrix = [['' for j in range(y)] for i in range(x)]

    for i in range(0, x):
        for j in range(0,y):
            rand = random.randint(0, jumlahToken-1)
            matrix[i][j] = listTokenFinal[rand]
    
    return matrix

def makeSequence(jumlahSekuens, maxSekuens, listTokenFinal, jumlahToken):
    listsequence = []

    for i in range(0, jumlahSekuens):
        temprand = random.randint(2, maxSekuens)
        temp = []
        for j in range(0, temprand):
            rand = random.randint(0, jumlahToken-1)
            temp.append(listTokenFinal[rand])
        listsequence.append(temp)
    
    return listsequence

def makeSequenceReward(jumlahSekuens):
    listReward = []

    for i in range(0, jumlahSekuens):
        listReward.append(random.randint(1, 10)*5)

    return listReward