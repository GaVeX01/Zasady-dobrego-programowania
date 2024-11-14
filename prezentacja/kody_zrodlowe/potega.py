print("Liczba | Kwadrat | Sześcian")
print("-----------------------------")
print(1, "    |", 1**2, "      |", 1**3)
print(2, "    |", 2**2, "      |", 2**3)
print(3, "    |", 3**2, "      |", 3**3)
print(4, "    |", 4**2, "     |", 4**3)
print(5, "    |", 5**2, "     |", 5**3)
print(6, "    |", 6**2, "     |", 6**3)
print(7, "    |", 7**2, "     |", 7**3)
print(8, "    |", 8**2, "     |", 8**3)
print(9, "    |", 9**2, "     |", 9**3)
print(10, "   |", 10**2, "    |", 10**3)

#-----------------------------------------------------------------

def potegi(liczba): # funkcja zwraca potege i kwadrat podanej liczby
    kwadrat = liczba ** 2 # ** 2 to kwadrat liczby
    szescian = liczba ** 3 # ** 3 to szescian
    return kwadrat, szescian # zwracamy liczby

def wypisz_tabelke():
    print("Liczba | Kwadrat | Sześcian") # linia naglowkowa tabeli i linia oddzielajaca
    print("-----------------------------")
    for liczba in range(1, 11):
        kwadrat, szescian = potegi(liczba)
        print(f"{liczba:<6} | {kwadrat:<7} | {szescian}") # wypisujemy w pętli wartosci zapis {liczba:<6} to formatowanie tekstu.

wypisz_tabelke()
