def fibonacci_overflow(max_value):
    a, b = 0, 1
    index = 1
    
    while True:
        # Symulacja ograniczenia zakresu zmiennej
        if b > max_value:
            print(f"Błąd: przekroczono zakres zmiennej przy liczbie {b} w indeksie {index}")
            break
        print(f"F({index}) = {b}")
        a, b = b, a + b
        index += 1

# Ustalmy maksymalną wartość zmiennej na np. 100000, aby szybko zauważyć błąd
fibonacci_overflow(100000)
