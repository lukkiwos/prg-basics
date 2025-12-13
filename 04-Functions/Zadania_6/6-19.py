from collections import Counter

def f(number):
    # 1. Konwersja liczby na ciąg znaków, a następnie na Counter
    number_str = str(number)
    counts = Counter(number_str)
    
    total_sum = 0
    
    # 2. Iteracja przez policzone cyfry (jako klucze w Counter)
    for digit_char, count in counts.items():
        
        # 3. Sprawdzenie warunku powtórzenia (cyfra wystąpiła więcej niż raz)
        if count > 1:
            # Dodajemy wartość numeryczną cyfry do sumy
            # Musimy skonwertować znak cyfry z powrotem na liczbę całkowitą (np. '5' -> 5)
            total_sum += int(digit_char)
            
    return total_sum

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: f(1027)
# Cyfry: 1, 0, 2, 7. Żadna się nie powtarza. Oczekiwany wynik: 0
result1 = f(1027)
print(f"f(1027) returns {result1}")

# Przykład 2: f(230335)
# Cyfry powtarzające się: 3 (występuje 3 razy). Suma powtarzających się cyfr: 3. Oczekiwany wynik: 3
result2 = f(230335)
print(f"f(230335) returns {result2}")

# Przykład 3: f(513553007)
# Cyfry powtarzające się: 5 (występuje 3 razy), 3 (występuje 2 razy), 0 (występuje 2 razy).
# Suma powtarzających się cyfr: 5 + 3 + 0 = 8. Oczekiwany wynik: 8
#
# UWAGA: W treści zadania "Sample result" podano, że f(513553007) returns 21. 
# Zgodnie z definicją ("sum of repeated digits") 5+3+0=8. 
# Aby uzyskać 21, należałoby sumować wszystkie wystąpienia powtarzających się cyfr: 
# (5 * 3) + (3 * 2) + (0 * 2) = 15 + 6 + 0 = 21. 
# Będę trzymał się interpretacji: suma wszystkich wystąpień powtarzających się cyfr, 
# aby uzyskać wynik 21, ponieważ jest to bardziej prawdopodobne, co miał na myśli autor zadania.

def f_adjusted(number):
    """
    Zwraca sumę wszystkich wystąpień cyfr, które powtarzają się w danej liczbie.
    (Interpretacja w celu uzyskania wyniku 21 dla przykładu f(513553007)).
    """
    number_str = str(number)
    counts = Counter(number_str)
    
    total_sum = 0
    
    for digit_char, count in counts.items():
        if count > 1:
            # Dodajemy wartość cyfry 'count' razy
            digit_value = int(digit_char)
            total_sum += digit_value * count
            
    return total_sum

# Testowanie z interpretacją, która daje wynik 21:
result3_adjusted = f_adjusted(513553007)
print(f"f(513553007) returns {result3_adjusted}")

# Testowanie z interpretacją, która daje wynik 9:
# W przykładzie 230335: powtarza się tylko 3. Aby uzyskać 9, musiałoby być (3 * 3) = 9.
# Wróćmy do najbardziej prawdopodobnej interpretacji: 
# suma wartości unikalnych cyfr powtarzających się (dla f(230335) powinno być 3). 
# Aby uzyskać 9, co jest podane w "Sample result" dla f(230335), musimy użyć innej logiki.
# Prawdopodobnie cyfra 3 w 230335 była liczona jako 3+3+3=9, mimo że 3 jest jedyną powtarzającą się.

# Trzymając się logiki (powtarzająca się cyfra * jej liczba wystąpień):
# f(230335): (3 * 3) = 9. OK.
# f(513553007): (5 * 3) + (3 * 2) + (0 * 2) = 15 + 6 + 0 = 21. OK.

# Używamy poprawnej funkcji f_adjusted:
print("\n--- Ostateczne testy z poprawioną logiką (dającą 9 i 21) ---")
print(f"f(230335) returns {f_adjusted(230335)}")
print(f"f(513553007) returns {f_adjusted(513553007)}")