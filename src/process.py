import numpy as np
import random

def processInput(jumlahToken, listTokenFinal, maxBuffer, x, y, jumlahSekuens, maxSekuens):
    matrix = [['' for j in range(y)] for i in range(x)]

    for i in range(0, x):
        for j in range(0,y):
            rand = random.randint(0, jumlahToken-1)
            matrix[i][j] = listTokenFinal[rand]

    print(matrix)