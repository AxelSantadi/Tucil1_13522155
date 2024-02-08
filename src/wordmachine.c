#include "wordmachine.h"

boolean EndWord;
Word currentWord;

void IgnoreBlanks()
{
    /* Mengabaikan satu atau beberapa BLANK
        I.S. : currentChar sembarang
        F.S. : currentChar ≠ BLANK atau currentChar = MARK */

    while (currentChar == BLANK)
    {
        ADV();
    }
}

void STARTWORD()
{
    /* I.S. : currentChar sembarang
       F.S. : EndWord = true, dan currentChar = MARK;
              atau EndWord = false, currentWord adalah kata yang sudah diakuisisi,
              currentChar karakter pertama sesudah karakter terakhir kata */
    
    START();
    IgnoreBlanks();

    if (currentChar == MARK)
    {
        EndWord = true;
    }
    else
    {
        CopyWord();
        IgnoreBlanks();
    }
}

void ADVWORD()
{
   /* I.S. : currentChar adalah karakter pertama kata yang akan diakuisisi
      F.S. : currentWord adalah kata terakhir yang sudah diakuisisi,
             currentChar adalah karakter pertama dari kata berikutnya, mungkin MARK
             Jika currentChar = MARK, EndWord = true.
      Proses : Akuisisi kata menggunakan procedure SalinWord */
      
    CopyWord();
    IgnoreBlanks();
    if (currentChar == MARK)
    {
        EndWord = true;
    }
}

void CopyWord()
{
   /* Mengakuisisi kata, menyimpan dalam currentWord
      I.S. : currentChar adalah karakter pertama dari kata
      F.S. : currentWord berisi kata yang sudah diakuisisi;
             currentChar = BLANK atau currentChar = MARK;
             currentChar adalah karakter sesudah karakter terakhir yang diakuisisi.
             Jika panjang kata melebihi NMax, maka sisa kata "dipotong" */

    int i = 0;
    while (currentChar != BLANK && !EOP && i < NMax)
    {
        currentWord.TabWord[i] = currentChar;
        ADV();
        i++;
    }

    if (i >= NMax)
    {
        currentWord.Length = NMax;
    }
    else
    {
        currentWord.Length = i;
    }
}