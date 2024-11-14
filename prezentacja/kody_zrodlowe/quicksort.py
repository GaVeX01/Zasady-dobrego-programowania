import random  # Importujemy moduł random, aby móc losować liczby

# Ustawiamy rozmiar tablicy
N = 100

# Tworzymy pustą tablicę D o rozmiarze N
D = []

# Losujemy 100 liczb pseudolosowych z przedziału 0-49 i dodajemy je do tablicy D
for _ in range(N):
    liczba = random.randint(0, 49)  # Losujemy liczbę z przedziału 0-49
    D.append(liczba)                # Dodajemy wylosowaną liczbę do tablicy

# Funkcja quicksort
def quicksort(tablica):
    # Jeśli tablica ma długość 1 lub 0, jest już posortowana
    if len(tablica) <= 1:
        return tablica
    
    # Wybieramy pivot, tutaj używamy środka tablicy
    pivot = tablica[len(tablica) // 2]
    
    # Dzielimy elementy tablicy na trzy listy:
    # - mniejsze od pivota,
    # - równe pivotowi,
    # - większe od pivota.
    mniejsze = [x for x in tablica if x < pivot]  # wyrażenie listowe - składnia : [wyrażenie for element in lista if warunek]
    rowne = [x for x in tablica if x == pivot]    # skrócona forma petli for tworzaca nowa liste z elementami spelniajacymi warunek
    wieksze = [x for x in tablica if x > pivot]   #
    
    # Rekurencyjnie sortujemy mniejsze i większe elementy, a następnie łączymy
    return quicksort(mniejsze) + rowne + quicksort(wieksze)

# Wyświetlamy tablicę przed sortowaniem
print("Tablica przed sortowaniem:")
print(D)

# Sortujemy tablicę D za pomocą quicksort
D = quicksort(D)

# Wyświetlamy tablicę po sortowaniu
print("\nTablica po sortowaniu:")
print(D)
