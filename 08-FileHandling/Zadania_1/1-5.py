
# Krok 1: Odczyt pliku i utworzenie listy
with open('countries.txt', 'r') as file:
    # Odczytujemy wszystkie linie. Funkcja readlines() zwraca listę ciągów znaków.
    # Używamy list comprehension, aby usunąć znak nowej linii ('\n') na końcu każdej linii.
    content = [line.strip() for line in file.readlines()]

# Krok 2: Numerowanie i wyświetlanie listy (używając enumerate)
print("\n--- Numerowana lista z pliku ---")

for numer, element in enumerate(content, start=1):
    # Sprawdzamy, czy element nie jest pustą linią (np. na końcu pliku)
    if element:
        print(f"{numer}. {element}")