import sys
sys.path.insert(0, 'C:/Users/Axel Santadi/Documents/Cool_Yeah/Tingkat_2/Semester_4/StiMa/Tucil/01/Tucil1_13522155/src')

#abaikan kuning2 ini kak, anehnya it works, so.. yeah, if it works it works i guess. 🤷‍♂️
import readFile
import cli
import brute
import time

nput = input("Apakah anda ingin memasukkan Input atau membaca .txt? (Input / Text / Gajadi): ")

while (nput != "Input" and nput != "Text" and nput != "Gajadi"):
    nput = input("Ngomong opo toh mazzeh? Diketik lagi coba (Input / Text / Gajadi): ")

if (nput == "Text"):
    nama1 = "C:\\Users\\Axel Santadi\\Documents\\Cool_Yeah\\Tingkat_2\\Semester_4\\StiMa\\Tucil\\01\\Tucil1_13522155\\bin\\"
    nama2 = input("Masukkan nama file yang ingin anda baca (akhiri dengan .txt): ")
    namafile = nama1 + nama2
    data = readFile.baca_file(namafile)
    tucil = readFile.proses_data(data)

    cli.checkData(tucil)

    route = []
    routePoints = []
    visited = [[False]*tucil.col for _ in range(tucil.row)]  # Initialize visited matrix

    # Iterate through all starting points in the top row
    start = time.time()

    for j in range(tucil.col):
        brute.search_route(tucil, tucil.matriks, 0, j, route, routePoints, visited, tucil.buffer, True)

    # Output the route with the maximum reward
    print("Max Reward: ", brute.max_reward)
    print("Max Route: ", end="")
    for i in range(len(brute.max_route)):
        print(brute.max_route[i], end=" ")
    print()
    print("Max Route Coordinates: ", end="")
    for point in brute.max_route_coordinates:
        print(f'({point.row + 1}, {point.col + 1})', end=" ")
    print()

    stop = time.time()
    duration = stop - start
    print("Execution time: ", duration, " seconds")

    save = input("apakah hasil ini mau anda simpan ke dalam file? (Y/N): ")

    if (save == "Y"):
        nama3 = "C:\\Users\\Axel Santadi\\Documents\\Cool_Yeah\\Tingkat_2\\Semester_4\\StiMa\\Tucil\\01\\Tucil1_13522155\\test\\"
        nama4 = input("Masukkan nama file yang ingin anda simpan (akhiri dengan .txt): ")
        namafile2 = nama3 + nama4    
        brute.write_sequence_to_file(namafile2, brute.max_route, brute.max_reward, brute.max_route_coordinates, duration)

        print("okay, file sudah tersimpan di folder test dengan nama", nama4 + ". Terima kasih sudah menggunakan program ini, sampai jumpa lagi :D .")
    elif(save == "N"):
        print("Okay, Terima kasih sudah menggunakan program ini, sampai jumpa lagi :D .")

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

    matriks = cli.generateMatriks(readFile.Tucil(maxBuffer, x, y, jumlahSekuens, maxSekuens, [], [], []), listTokenFinal, jumlahToken)
    sequence = cli.generateSequence(readFile.Tucil(maxBuffer, x, y, jumlahSekuens, maxSekuens, matriks, [], []), listTokenFinal, jumlahToken)
    reward_sequence = cli.generateRewardSequence(readFile.Tucil(maxBuffer, x, y, jumlahSekuens, maxSekuens, matriks, sequence, []))
    tucil = readFile.Tucil(maxBuffer, x, y, jumlahSekuens, maxSekuens, matriks, sequence, reward_sequence)

    cli.checkData(tucil)

    route = []
    routePoints = []
    visited = [[False]*tucil.col for _ in range(tucil.row)]  # Initialize visited matrix

    # Iterate through all starting points in the top row
    start = time.time()

    for j in range(tucil.col):
        brute.search_route(tucil, tucil.matriks, 0, j, route, routePoints, visited, tucil.buffer, True)

    # Output the route with the maximum reward
    print("Max Reward: ", brute.max_reward)
    print("Max Route: ", end="")
    for i in range(len(brute.max_route)):
        print(brute.max_route[i], end=" ")
    print()
    print("Max Route Coordinates: ", end="")
    for point in brute.max_route_coordinates:
        print(f'({point.row + 1}, {point.col + 1})', end=" ")
    print()

    stop = time.time()
    duration = stop - start
    print("Execution time: ", duration, " seconds")

    save = input("apakah hasil ini mau anda simpan ke dalam file? (Y/N): ")

    if (save == "Y"):
        nama3 = "C:\\Users\\Axel Santadi\\Documents\\Cool_Yeah\\Tingkat_2\\Semester_4\\StiMa\\Tucil\\01\\Tucil1_13522155\\test\\"
        nama4 = input("Masukkan nama file yang ingin anda simpan (akhiri dengan .txt): ")
        namafile2 = nama3 + nama4    
        brute.write_sequence_to_file(namafile2, brute.max_route, brute.max_reward, brute.max_route_coordinates, duration)
        print("okay, file sudah tersimpan di folder test dengan nama", nama4 + ". Terima kasih sudah menggunakan program ini, sampai jumpa lagi :D .")
    elif(save == "N"):
        print("Okay, Terima kasih sudah menggunakan program ini, sampai jumpa lagi :D .")

elif (nput == "Gajadi"):
    print("Oke deh masbro, see you next time :D .")