#include <iostream>
extern "C" {
    #include "matrix.h"
    #include "matrix.c"
    #include "charmachine.h"
    #include "wordmachine.h"
    #include "wordmachine.c"
    #include "charmachine.c"
}
#include <fstream>
#include <string>
#include "readfile.cpp"

int main()
{
    std::string nput;
    std::cout << "Apakah anda ingin memasukkan Input atau membaca .txt? (Input / Text / Gajadi) : ";
    std::cin >> nput;

    while (nput != "Input" && nput != "Text" && nput != "Gajadi")
    {
        std::cout << "Ngomong opo toh mazzeh";
        std::cin >> nput;
    }

    if (nput == "Text")
    {
        readfile();
    }
    else if (nput == "Input")
    {
        int jumlahToken, maxBuffer, x, y, jumlahSekuens, maxSekuens;
        Matrix m;
        std::cout << "Masukkan jumlah token unik: ";
        std::cin >> jumlahToken;
        std::cout << "Masukkan token apa saja yang akan dipakai: ";
        std::cout << "Masukkan jumlah buffer maksimal: ";
        std::cin >> maxBuffer;
        std::cout << "Masukkan ukuran matrix: ";
        std::cin >> x;
        std::cin >> y;
        createMatrix(x, y, &m);
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                ELMT(m,i,j) = i + j;
            }
        }
        displayMatrix(m);
        std::cout << "Masukkan jumlah sekuens: ";
        std::cin >> jumlahSekuens;
        std::cout << "Masukkan ukuran maksimal sekuens: ";
        std::cin >> maxSekuens;
    }
    else if (nput == "Gajadi")
    {
        std::cout << "Oke deh masbro, see you next time :D .";
    }

    return 0;
}