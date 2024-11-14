#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];  // Bufor o rozmiarze 10 znaków

    // Funkcja strcpy nie sprawdza, czy rozmiar źródła pasuje do bufora
    strcpy(buffer, "To jest długi tekst, który przekracza 10 znaków!");

    printf("Zawartość bufora: %s\n", buffer);
    return 0;
}
