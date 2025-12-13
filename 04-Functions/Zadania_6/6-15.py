
def f(detector):
    current_occupants = 0
    max_occupants = 0
    
    for event in detector:
        
        if event == '+':
            # Wejście do pomieszczenia
            current_occupants += 1
            
        elif event == '-':
            # Wyjście z pomieszczenia
            # Zakładamy, że liczba osób nie spadnie poniżej zera
            current_occupants -= 1
        
        # Aktualizujemy maksymalną zaobserwowaną liczbę osób
        if current_occupants > max_occupants:
            max_occupants = current_occupants
            
        # Optymalizacja: jeśli osiągnęliśmy już warunek (>= 3), możemy zakończyć
        if max_occupants >= 3:
            # Zwracamy True, gdy tylko warunek zostanie spełniony
            return True

    # Jeśli pętla się zakończyła i nigdy nie osiągnięto 3 osób
    return max_occupants >= 3


# --- Przykłady użycia ---

# Przykład 1: Maksymalnie 3 osoby (+, +, +, -, -, +) -> True
# Stan: 1, 2, 3, 2, 1, 2. Max: 3
result1 = f("+++--+")
print(f"f('+++--+') returns {result1}") 

# Przykład 2: Maksymalnie 2 osoby (+, +, -, -) -> False
# Stan: 1, 2, 1, 0. Max: 2
result2 = f("++--")
print(f"f('++--') returns {result2}")

# Przykład 3: Bardziej złożony ciąg -> True
# Stan: 1, 2, 3, 4, 3, 2. Max: 4
result3 = f("+ + + + - -")
print(f"f('+ + + + - -') returns {result3}")

# Przykład 4: Ciąg, w którym nigdy nie ma 3 osób
result4 = f("+-+-+-")
print(f"f('+-+-+-') returns {result4}")