def f(password):
    # Krok 1: Sprawdzenie długości (co najmniej 6 znaków)
    if len(password) < 6:
        return False
        
    # Krok 2: Sprawdzenie unikalności znaków
    # Tworzymy zbiór (set) z hasła. Zbiór automatycznie usuwa duplikaty.
    unique_chars = set(password)
    
    # Jeśli długość oryginalnego hasła jest większa niż długość zbioru
    # (czyli usunięte zostały duplikaty), hasło jest niepoprawne.
    if len(password) != len(unique_chars):
        return False
        
    # Jeśli oba warunki zostały spełnione
    return True

# --- Przykłady użycia (zgodnie z Sample result) ---

# 1. Za krótkie i z duplikatem ('xx15')
result1 = f("xx15")
print(f"f('xx15') returns {result1}")

# 2. Poprawna długość, ale z duplikatem ('book123')
result2 = f("book123")
print(f"f('book123') returns {result2}")

# 3. Poprawna długość, unikalne znaki ('A2water3')
result3 = f("A2water3")
print(f"f('A2water3') returns {result3}")

# 4. Poprawna długość, unikalne znaki ('qwerty')
result4 = f("qwerty")
print(f"f('qwerty') returns {result4}")
