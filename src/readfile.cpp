#include <iostream>
#include <fstream>
#include <string>

void readfile()
{
    std::string nama1 = "C:\\Users\\Axel Santadi\\Documents\\Cool_Yeah\\Tingkat_2\\Semester_4\\StiMa\\Tucil\\01\\Tucil1_13522155\\src\\";
    std::cout << "Masukkan nama file teks (.txt): ";
    std::string nama2;
    std::cin >> nama2;

    //Tambahkan ekstensi .txt jika pengguna tidak memasukkan
    if (nama2.find(".txt") == std::string::npos)
    {
        nama2 += ".txt";
    }

    // Membuka file
    std::ifstream file(nama1 + nama2);
    
    // Memeriksa apakah file berhasil dibuka
    if (!file.is_open())
    {
        std::cerr << "Gagal membuka file." << std::endl;
    }

    std::string line;
    std::cout << "Isi dari file " << (nama2) << ":\n";
    // Membaca dan mencetak isi file baris per baris
    while (std::getline(file, line))
    {
        std::cout << line << std::endl;
    }

    // Menutup file
    file.close();
}
