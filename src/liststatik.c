#include <stdio.h>
#include <stdlib.h>
#include "boolean.h"
#include "liststatik.h"

ElType staticmark = {"",-1};

/* ********** KONSTRUKTOR ********** */
/* Konstruktor : create List kosong  */
void CreateListStatik(ListStatik *l)
/* I.S. l sembarang */
/* F.S. Terbentuk List l kosong dengan kapasitas CAPACITY */
/* Proses: Inisialisasi semua elemen List l dengan MARK */
{
   int i;
   for (i = 0; i < CAPACITY; i++)
   {
      SELMT(*l, i) = staticmark;
   }
}

/* ********** BACA dan TULIS dengan INPUT/OUTPUT device ********** */

/* *** Mendefinisikan isi List dari pembacaan *** */
void readList(ListStatik *l)
/* I.S. l sembarang */
/* F.S. List l terdefinisi */
/* Proses: membaca banyaknya elemen l dan mengisi nilainya */
/* 1. Baca banyaknya elemen diakhiri enter, misalnya n */
/*    Pembacaan diulangi sampai didapat n yang benar yaitu 0 <= n <= CAPACITY */
/*    Jika n tidak valid, tidak diberikan pesan kesalahan */
/* 2. Jika 0 < n <= CAPACITY; Lakukan n kali: 
          Baca elemen mulai dari indeks 0 satu per satu diakhiri enter */
/*    Jika n = 0; hanya terbentuk List kosong */
{
   int n, i, index;
   index = 0;
   n = 0;
   scanf("%d", &n);

   while ((n < 0) || (n > CAPACITY))
   {
      scanf("%d", &n);
   }
   
   CreateListStatik(l);
   if (n != 0)
   {
      for (i = 1; i <= n; i++)
      {
         CopyWord();
         SELMT(*l, index) = currentWord;
         index++;
      }
   }
}

int getLastIdx(ListStatik l)
{
   int i = 0;
   while (SELMT(l, i) != staticmark)
   {
      i++;
   }
   return i;
}

/* *** Menambahkan elemen terakhir *** */
void insertLast(ListStatik *l, ElType val)
/* Proses: Menambahkan val sebagai elemen terakhir List */
/* I.S. List l boleh kosong, tetapi tidak penuh */
/* F.S. val adalah elemen terakhir l yang baru */
{
   SELMT(*l, getLastIdx(*l)+1) = val;
}