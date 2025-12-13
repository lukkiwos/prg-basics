def sum_natural(n):
    if not isinstance(n, int) or n < 1:
        # Obsługa przypadku, gdy n nie jest liczbą naturalną
        return 0
    
    # Warunek bazowy
    if n == 1:
        return 1
    
    # Krok rekurencyjny
    return n + sum_natural(n - 1)

# --- Główna część programu ---

RANGE_MAX = 10

# Używamy funkcji rekurencyjnej do obliczenia sumy w zakresie <1, 10>
sum_result = sum_natural(RANGE_MAX)

print(f"Obliczenie sumy liczb naturalnych w zakresie <1, {RANGE_MAX}>:")
print(f"Suma (S({RANGE_MAX})) = {sum_result}")