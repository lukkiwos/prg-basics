# 1. Definicja tablicy wejściowej
arr = [8, 2, 5, 1, 9]

# 2. Inicjalizacja nowej, pustej tablicy na wyniki
second_power = []

# --- Wypisanie istniejącej tablicy (dla porównania) ---
print(f"Array: {arr}")

# 3. Użycie pętli for do przejrzenia każdego elementu
# W tej pętli 'liczba' to kolejne elementy: 8, 2, 5, 1, 9.
for number in arr:
    
    # 4. Obliczenie drugiej potęgi
    # Używamy operatora ** (potęgowanie) do podniesienia liczby do potęgi 2.
    druga_potega = number ** 2
    
    # 5. Dodanie wyniku do nowej tablicy
    second_power.append(druga_potega)

# 6. Wypisanie wyników
print("2nd power: ", end="")

# Wypisujemy zawartość wynikowej tablicy w jednej linii
for square in second_power:
    print(square, end=" ")
    
print("\n")