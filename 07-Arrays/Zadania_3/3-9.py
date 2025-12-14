# 1. Definicja funkcji porównującej dwie tablice (listy w Pythonie)
def compare(array1, array2):
    # Krok 1: Sprawdzenie długości
    if len(array1) != len(array2):
        print("  -> Różne długości: Tablice nie są równe.")
        return False
    
    # Jeśli długości są równe, przechodzimy do porównania elementów
    dlugosc = len(array1)
    print(f"  -> Długości są równe ({dlugosc}). Sprawdzam elementy...")
    
    # Krok 2: Porównanie elementów na każdej pozycji (indeksie)
    # Używamy pętli 'for' i funkcji range() do iterowania przez indeksy
    for i in range(dlugosc):
        # Sprawdzenie, czy elementy na bieżącym indeksie 'i' są różne
        if array1[i] != array2[i]:
            print(f"  -> Elementy na indeksie {i} są różne ({array1[i]} vs {array2[i]}).")
            return False  # Jeśli znajdziemy choć jedną różnicę, natychmiast zwracamy False
            
    # Jeśli pętla zakończy się bez zwrócenia False, oznacza to, że wszystkie elementy są równe
    print("  -> Wszystkie elementy są równe.")
    return True

# --- Zestaw danych testowych ---
pary_tablic = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 9, 3], [5, 9, 3])
]

# 3. Testowanie funkcji dla podanych par
print("--- Wyniki porównania tablic ---")

for numer, (arr1, arr2) in enumerate(pary_tablic, 1):
    print(f"\nPorównanie {numer}:")
    
    # 4. Wypisanie tablic
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # Wywołanie funkcji i zapisanie wyniku
    rezultat = compare(arr1, arr2)
    
    # Wypisanie wyniku porównania
    print(f"Result of comparison: {rezultat}")