def divide_by_user_input():
    # Pobranie liczby od użytkownika
    number = float(input("Podaj liczbę: "))
    
    # Próba podzielenia 10 przez podaną liczbę
    result = 10 / number
    
    print(f"Wynik dzielenia 10 przez {number} to: {result}")

# Wywołanie funkcji
divide_by_user_input()
