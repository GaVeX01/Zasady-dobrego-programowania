def buffer_overflow_simulation():
    # Ustawiamy bufor o rozmiarze 5 elementów
    buffer = [0] * 5

    # Wyświetlamy początkowy stan bufora
    print("Początkowy bufor:", buffer)

    # Próbujemy zapisać wartość poza zakresem bufora (indeks poza 4)
    try:
        for i in range(7):  # Celowo wychodzimy poza zakres bufora
            buffer[i] = i * 10
            print(f"Zapis do bufora[{i}] = {i * 10}")
    except IndexError as e:
        print("Błąd przepełnienia bufora:", e)

    # Wyświetlamy ostateczny stan bufora
    print("Ostateczny bufor:", buffer)

# Uruchomienie symulacji
buffer_overflow_simulation()
