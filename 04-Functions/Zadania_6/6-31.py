def power(x, n):
    # Obsługa ujemnych wykładników (opcjonalna, ale dobra praktyka)
    if n < 0:
        # x^-n = 1 / x^n
        return 1 / power(x, -n)
    
    # Warunek bazowy: x^0 = 1
    if n == 0:
        return 1
    
    # Krok rekurencyjny: x^n = x * x^(n-1)
    return x * power(x, n - 1)

# --- Główna część programu ---

BASE = 5
EXPONENT = 3

# Używamy funkcji rekurencyjnej do obliczenia 5^3
result = power(BASE, EXPONENT)

print(f"Obliczenie {BASE} do potęgi {EXPONENT} rekurencyjnie:")
print(f"{BASE}^{EXPONENT} = {result}")