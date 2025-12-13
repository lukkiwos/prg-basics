def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: Co najmniej jedna liczba jest ujemna (n3 = -4)
result1 = f(1, 6, -4)
print(f"f(1, 6, -4) returns {result1}")

# Przykład 2: Wszystkie liczby są dodatnie
result2 = f(5, 4, 14)
print(f"f(5, 4, 14) returns {result2}")