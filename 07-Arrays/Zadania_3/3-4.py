# 1. Definicja tablicy wejściowej
arr = [-15, 8, -31, 47, -2, 19]

# 2. Inicjalizacja: Ustawienie maksimum i minimum na pierwszy element tablicy
# To bezpieczny sposób, który działa dla tablic zawierających zarówno liczby dodatnie, jak i ujemne.
maksimum = arr[0] # Początkowo: -15
minimum = arr[0]  # Początkowo: -15

print(f"Tablica wejściowa: {arr}")

# 3. Użycie pętli for do przejrzenia WSZYSTKICH elementów
# Alternatywnie można zacząć od indeksu 1, ale prościej jest przeglądać od początku.
for liczba in arr:
    
    # 4a. Sprawdzenie maksimum
    # Jeśli obecna liczba jest większa niż dotychczasowe maksimum
    if liczba > maksimum:
        maksimum = liczba  # Zaktualizuj maksimum
        
    # 4b. Sprawdzenie minimum
    # Jeśli obecna liczba jest mniejsza niż dotychczasowe minimum
    if liczba < minimum:
        minimum = liczba  # Zaktualizuj minimum

# 5. Wypisanie wyników
print(f"Wartość maksymalna w tablicy: {maksimum}")
print(f"Wartość minimalna w tablicy: {minimum}")