def f(product_code):
    # Krok 1: Sprawdzenie długości i formatu
    if len(product_code) != 4 or not product_code.isdigit():
        return False # Niepoprawny format

    # Krok 2: Konwersja cyfr na liczby całkowite
    # Python pozwala na bezpośredni dostęp do znaków ciągu
    c1 = int(product_code[0])
    c2 = int(product_code[1])
    c3 = int(product_code[2])
    c4_actual = int(product_code[3]) # Rzeczywista cyfra kontrolna
    
    # Krok 3: Obliczenie oczekiwanej cyfry kontrolnej
    sum_of_first_three = c1 + c2 + c3
    c4_expected = sum_of_first_three % 7
    
    # Krok 4: Porównanie
    return c4_actual == c4_expected

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: "1882" (Poprawny)
# Suma: 1 + 8 + 8 = 17. Oczekiwana C4: 17 % 7 = 3. Rzeczywista C4: 2. -> FALSE
# UWAGA: W Sample Result jest '1882' returns True. Sprawdźmy: 1+8+8=17. 17%7=3. 
# W tym przypadku 2 != 3, co oznacza, że przykład z treści zadania jest BŁĘDNY. 
# Założę, że poprawna logika jest ważniejsza niż błędny przykład i zwrócę False.
# (Jeśli miałoby zwrócić True, kod powinien być np. "1883")
result1 = f("1882")
print(f"f('1882') returns {result1}") # Oczekiwany True, wg. logiki False

# Przykład 2: "2035" (Poprawny)
# Suma: 2 + 0 + 3 = 5. Oczekiwana C4: 5 % 7 = 5. Rzeczywista C4: 5. -> TRUE
result2 = f("2035")
print(f"f('2035') returns {result2}")

# Przykład 3: "1114" (Niepoprawny)
# Suma: 1 + 1 + 1 = 3. Oczekiwana C4: 3 % 7 = 3. Rzeczywista C4: 4. -> FALSE
result3 = f("1114")
print(f"f('1114') returns {result3}")

# Przykład 4: "7071" (Niepoprawny)
# Suma: 7 + 0 + 7 = 14. Oczekiwana C4: 14 % 7 = 0. Rzeczywista C4: 1. -> FALSE
result4 = f("7071")
print(f"f('7071') returns {result4}")

# Dodatkowy przykład (poprawny zgodnie z logiką)
# Kod: 1236. Suma: 1+2+3 = 6. Oczekiwana C4: 6 % 7 = 6. Rzeczywista C4: 6. -> TRUE
print(f"f('1236') returns {f('1236')}")