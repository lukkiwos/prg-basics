
# 1. Definicja tablicy z liczbami
arr = [15, 8, 31, 47, 2, 19]

# --- Wypisanie istniejącej tablicy ---
print(f"Existed array: {arr}")

# --- Użycie funkcji reversed() w pętli for ---
print("Reverse array: ", end="")

# Funkcja reversed(arr) zwraca elementy w kolejności 19, 2, 47, 31, 8, 15
for element in reversed(arr):
    # Drukujemy każdy element bez potrzeby zarządzania indeksami
    print(element, end=" ")
    
print("\n")