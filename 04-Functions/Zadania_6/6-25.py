def f(x, y):
    total_sum = 0
    
    # Pętla iteruje przez liczby od x do y włącznie (y + 1)
    for i in range(x, y + 1):
        
        # Warunek: (i % 2 == 0) and (i % 4 != 0) 
        # Optymalny warunek: i % 4 == 2
        if i % 4 == 2:
            total_sum += i
            
    return total_sum

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: Zakres [1, 20]
# Liczby spełniające warunek: 2, 6, 10, 14, 18.
# Suma: 2 + 6 + 10 + 14 + 18 = 50
# W przykładzie jest: f(1, 20) returns 24. Prawdopodobnie błąd w treści zadania, 
# ponieważ 2+6+10+14+18=50.
# Jeśli wynik 24 jest poprawny, to kryterium może być: Liczby parzyste w [1, 10] (2+4+6+8+10=30)
# lub np. tylko [1, 10] spełniające Twoje kryterium (2+6+10 = 18).
# Trzymamy się ściśle Twojego kryterium.

result1 = f(1, 20)
print(f"f(1, 20) returns {result1}")

# Przykład 2: Zakres [20, 30]
# Liczby spełniające warunek: 22, 26, 30.
# Suma: 22 + 26 + 30 = 78
result2 = f(20, 30)
print(f"f(20, 30) returns {result2}")

# Test z małym zakresem
result3 = f(1, 10)
print(f"f(1, 10) returns {result3}") # 2 + 6 + 10 = 18