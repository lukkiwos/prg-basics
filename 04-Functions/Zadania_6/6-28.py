def f(dice):
    if not dice:
        return None # Zwraca None dla pustego ciągu
        
    # Krok 1: Zliczanie wystąpień każdej cyfry
    counts = {}
    for roll in dice:
        # Zakładamy, że rzuty są cyframi, ale konwertujemy je na int 
        # tylko dla bezpieczeństwa lub sortowania wyników, 
        # ale przechowujemy jako stringi dla prostszej obsługi kluczy
        counts[roll] = counts.get(roll, 0) + 1
        
    # Krok 2: Znalezienie maksymalnej częstotliwości
    max_count = 0
    most_frequent_roll = None
    
    # Przechodzimy przez słownik (klucz = rzut, wartość = częstotliwość)
    # Zaczynamy od niższych wartości rzutów (sortując klucze), aby 
    # w przypadku remisu zwrócić niższy numer, co jest bezpieczniejsze.
    for roll in sorted(counts.keys()):
        count = counts[roll]
        
        # Jeśli aktualna częstotliwość jest większa od max_count, aktualizujemy
        if count > max_count:
            max_count = count
            most_frequent_roll = roll
            
    # Krok 3: Zwracamy wynik jako liczbę całkowitą
    return int(most_frequent_roll) if most_frequent_roll is not None else None

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: "523316554211"
# Wystąpienia: 1(3), 2(2), 3(2), 4(0), 5(3), 6(1). Max: 3 (dla 1 i 5). Zwraca 1 (bo jest mniejsze)
# UWAGA: W przykładzie f("523316554211") returns 5. Jeśli sortujemy po wartościach (cyfrach),
# 1 i 5 mają po 3 wystąpienia. W przypadku remisu algorytm powinien wybrać 5.
# Mój algorytm wybierze 1. Zmodyfikujmy, aby priorytetem była wartość, która 
# była pierwsza lub większa, aby uzyskać 5. Wróćmy do iteracji niesortowanej.

def f_modified(dice):
    counts = {}
    for roll in dice:
        counts[roll] = counts.get(roll, 0) + 1
    
    max_count = -1
    most_frequent_roll = -1
    
    # Iterujemy po słowniku (kolejność jest dowolna, ale Python 3+ ją zachowuje)
    # Sprawdzamy, czy mamy nową większą częstotliwość LUB taką samą,
    # ale aktualna wartość rzutu jest WIĘKSZA (aby dopasować się do f("52331...") -> 5)
    for roll_str, count in counts.items():
        roll_int = int(roll_str)
        
        if count > max_count:
            max_count = count
            most_frequent_roll = roll_int
        elif count == max_count and roll_int > most_frequent_roll:
            # W przypadku remisu, bierzemy większą wartość rzutu.
            max_count = count
            most_frequent_roll = roll_int
            
    return most_frequent_roll

# Przykład 1: "523316554211"
# Poprawiona logika: 1(3), 5(3). Wybrano 5, ponieważ 5 > 1.
result1 = f_modified("523316554211")
print(f"f('523316554211') returns {result1}")

# Przykład 2: "213316554211"
# Wystąpienia: 1(3), 2(2), 3(2), 5(2), 6(1). Max: 3 (dla 1).
result2 = f_modified("213316554211")
print(f"f('213316554211') returns {result2}")

# Przykład 3: "2133" (3 ma 2, 2 ma 1, 1 ma 1). Max: 3.
result3 = f_modified("2133")
print(f"f('2133') returns {result3}")