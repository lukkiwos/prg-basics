def f(expression):
    # 1. Inicjalizacja: Pierwsza liczba jest punktem startowym.
    # Musimy zamienić pierwszy znak na liczbę całkowitą (int).
    try:
        result = int(expression[0])
    except (ValueError, IndexError):
        return "Error: Invalid starting number in expression."
    
    # 2. Iteracja: Zaczynamy od indeksu 1 (pierwszy operator) i skaczemy co 2 znaki.
    # Struktura: [liczba] [operator] [liczba] [operator] [liczba] ...
    i = 1
    while i < len(expression):
        operator = expression[i]
        
        # Sprawdzamy, czy kolejny element jest dostępny i jest liczbą.
        try:
            number = int(expression[i+1])
        except (ValueError, IndexError):
            return "Error: Expression format is incorrect (missing number after operator)."
        
        # 3. Wykonanie operacji
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        else:
            return f"Error: Invalid operator '{operator}'"
        
        # Przechodzimy do następnego operatora (skok o 2: operator + liczba)
        i += 2
        
    return result

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: "2+3" = 5
result1 = f("2+3")
print(f"f('2+3') returns {result1}")

# Przykład 2: "8+9-1" = 16
result2 = f("8+9-1")
print(f"f('8+9-1') returns {result2}")

# Przykład 3: "2+2-5-6+4" = -3
result3 = f("2+2-5-6+4")
print(f"f('2+2-5-6+4') returns {result3}")

# Test z błędem w treści zadania: 6 zamiast 8
# f("2+2-5-6+4") returns 6 -> Prawidłowy wynik to -3.
# Wyświetlimy poprawny wynik -3, ale zwróć uwagę, że w Twoim przykładzie jest błąd.