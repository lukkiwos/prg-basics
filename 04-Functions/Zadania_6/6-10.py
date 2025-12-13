def f(x,y):
    count = 0
    for i in range(x, y + 1):
        if i < 0 and i % 2 == 0:
            count += 1
    return count
    
# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: Zakres [-7, 8]
# Ujemne i parzyste w tym zakresie: -6, -4, -2. Liczba: 3
result1 = f(-7, 8)
print(f"f(-7, 8) returns {result1}")

# Przykład 2: Zakres [-1, 1]
# Ujemne i parzyste w tym zakresie: brak. Liczba: 0
result2 = f(-1, 1)
print(f"f(-1, 1) returns {result2}")
