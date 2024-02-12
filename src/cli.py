import random
import time

def countWords(str):
    return len(str.split())

def generateMatriks(tucil, token, jumlah_token_unik):
    random.seed(time.time())
    matriks = [[token[random.randint(0, jumlah_token_unik-1)] for _ in range(tucil.col)] for _ in range(tucil.row)]
    return matriks

def generateSequence(tucil, token, jumlah_token_unik):
    random.seed(time.time())
    sequence = [[token[random.randint(0, jumlah_token_unik-1)] for _ in range(random.randint(2, tucil.sequence_length))] for _ in range(tucil.jumlah_sequence)]
    return sequence

def generateRewardSequence(tucil):
    random.seed(time.time())
    reward_sequence = [random.randint(0, 99) for _ in range(tucil.jumlah_sequence)]
    return reward_sequence

def checkData(tucil):
    print("\nBerikut adalah data yang dihasilkan: \n\n")
    print("Buffer size: ", tucil.buffer)
    print("Row matriks: ", tucil.row)
    print("Col matriks: ", tucil.col)
    print("\nMatriks: ")
    for i in range(tucil.row):
        for j in range(tucil.col):
            print(tucil.matriks[i][j], end=" ")
        print()
    print("\nJumlah sequence: ", tucil.jumlah_sequence)
    print("Sequence length: ", tucil.sequence_length)
    print("\nSequences: ")
    for i in range(tucil.jumlah_sequence):
        print("Sequence ", i+1, ": ", end="")
        for j in range(len(tucil.sequence[i])):
            print(tucil.sequence[i][j], end=" ")
        print()
    print("\nReward sequences: ")
    for i in range(tucil.jumlah_sequence):
        print("Sequence ", i+1, ": ", tucil.reward_sequence[i])
    print()