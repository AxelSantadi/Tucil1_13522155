import readFile
import cli
import numpy as np

nput = input("Apakah anda ingin memasukkan Input atau membaca .txt? (Input / Text / Gajadi): ")

while (nput != "Input" and nput != "Text" and nput != "Gajadi"):
    nput = input("Ngomong opo toh mazzeh? Diketik lagi coba (Input / Text / Gajadi): ")

if (nput == "Text"):
    nama1 = "C:\\Users\\Axel Santadi\\Documents\\Cool_Yeah\\Tingkat_2\\Semester_4\\StiMa\\Tucil\\01\\Tucil1_13522155\\src\\"
    nama2 = input("Masukkan nama file yang ingin anda baca (akhiri dengan .txt): ")
    namafile = nama1 + nama2
    data = readFile.baca_file(namafile)
    buffer_size, matrix_width, matrix_height, matrix, num_sequences, sequences, rewards = readFile.proses_data(data)

elif (nput == "Input"):
    jumlahToken = int(input("Masukkan jumlah token unik: "))
    listToken = input("Masukkan token apa saja yang akan dipakai: ")
    listTokenFinal = listToken.split()
    maxBuffer = int(input("Masukkan jumlah buffer maksimal: "))
    listUkuranMatrix = input("Masukkan ukuran matrix: ")
    listUkuranMatrixFinal = listUkuranMatrix.split()
    x = int(listUkuranMatrixFinal[0])
    y = int(listUkuranMatrixFinal[1])
    jumlahSekuens = int(input("Masukkan jumlah sekuens: "))
    maxSekuens = int(input("Masukkan ukuran maksimal sekuens: "))
    while (maxSekuens <= 1):
        maxSekuens = int(input("Walaheh, 'sekuens' minimal 2 loh mazzeh, coba masukkin lagi: "))

    matrix = cli.makeMatrix(jumlahToken, listTokenFinal, x, y)
    listSequence = cli.makeSequence(jumlahSekuens, maxSekuens, listTokenFinal, jumlahToken)
    listReward = cli.makeSequenceReward(jumlahSekuens)

elif (nput == "Gajadi"):
    print("Oke deh masbro, see you next time :D .")