def f(n):
    # Przypadek brzegowy 1: F1 = 0
    if n == 1:
        return 0
    
    # Przypadek brzegowy 2: F2 = 1
    if n == 2:
        return 1

    # Inicjalizacja dla F(n-2) i F(n-1)
    a = 0  # Reprezentuje F(i-2)
    b = 1  # Reprezentuje F(i-1)
    
    # Pętla zaczyna się od F3, więc wykonujemy n-2 iteracji
    for _ in range(3, n + 1):
        # Obliczenie F(i)
        next_term = a + b
        
        # Aktualizacja zmiennych
        a = b          # Poprzednie F(i-1) staje się nowym F(i-2)
        b = next_term  # Nowe F(i) staje się nowym F(i-1)
        
    return b

# --- Przykłady użycia (zgodnie z Sample result) ---

# F5 = 3
result1 = f(5)
print(f"f(5) returns {result1}")

# F9 = 21
result2 = f(9)
print(f"f(9) returns {result2}")