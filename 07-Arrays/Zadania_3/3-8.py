# Definicja tablicy z danymi wejściowymi
arr = [2, 6, 4, 9, 7]

# 1. Definicja funkcji, która zwraca ciąg n gwiazdek
def star(n):
    ciag_gwiazdek = "*" * n
    return ciag_gwiazdek

# 2. Główny program: Iteracja przez tablicę i użycie funkcji
print("--- Graficzne przedstawienie wartości tablicy ---")

# Używamy pętli 'for' do przejścia przez każdy element w tablicy
for liczba in arr:
    gwiazdki = star(liczba)

    print(f"{liczba}: {gwiazdki}")

print("\n--- Zakończono ---")