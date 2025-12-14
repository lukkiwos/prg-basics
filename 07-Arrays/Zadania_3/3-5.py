# 1. Definicja tablicy z podanymi wartościami
arr = [15, 8, 31, 47, 2, 19]

# 2. Inicjalizacja zmiennej do sumowania elementów
suma = 0

# 3. Użycie pętli 'for' do przejścia przez każdy element tablicy i obliczenia sumy
print("--- Obliczenia ---")
for element in arr:
    # Dodanie aktualnego elementu do sumy
    suma += element 
    print(f"Dodaję: {element}. Aktualna suma: {suma}")

# Liczba elementów w tablicy (n)
liczba_elementow = len(arr)

# 4. Obliczenie średniej arytmetycznej
# Ważne: dzielenie musi być wykonane tak, aby wynik był liczbą zmiennoprzecinkową (używamy operatora '/')
srednia_arytmetyczna = suma / liczba_elementow

# Wypisanie wyników zgodnie z wymaganiami
print("\n--- Wynik ---")
print(f"Tablica: {arr}")
print(f"Suma elementów: {suma}")
print(f"Liczba elementów: {liczba_elementow}")
print(f"Średnia arytmetyczna wartości tablicy: {srednia_arytmetyczna}")