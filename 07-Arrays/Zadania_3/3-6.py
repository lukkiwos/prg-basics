# 1. Definicja tablicy z podanymi wartościami
arr = [15, 8, 31, 47, 2, 19]

# 2. Inicjalizacja zmiennej do sumowania elementów
suma = 0

# 3. Inicjalizacja indeksu dla pętli 'while'
indeks = 0

# Liczba elementów w tablicy (potrzebna do warunku pętli i obliczenia średniej)
liczba_elementow = len(arr)

# 4. Użycie pętli 'while' do przejścia przez każdy element tablicy
print("--- Obliczenia ---")
while indeks < liczba_elementow:
    
    # Pobranie aktualnego elementu tablicy
    aktualna_liczba = arr[indeks]
    
    # Dodanie aktualnego elementu do sumy
    suma += aktualna_liczba 
    print(f"Dodaję: {aktualna_liczba}. Aktualna suma: {suma}")
    
    # Ważne: Zwiększenie indeksu, aby przejść do następnego elementu
    indeks += 1 

# 5. Obliczenie średniej arytmetycznej
# Dzielimy sumę przez liczbę elementów.
srednia_arytmetyczna = suma / liczba_elementow

# Wypisanie wyników zgodnie z wymaganiami
print("\n--- Wynik ---")
print(f"Tablica: {arr}")
print(f"Suma elementów: {suma}")
print(f"Liczba elementów: {liczba_elementow}")
print(f"Średnia arytmetyczna wartości tablicy: {srednia_arytmetyczna}")