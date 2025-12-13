def fibonacci_sequence(count):
    # Drukuje pierwsze 'count' wyrazów ciągu Fibonacciego.

    # Pierwszy i drugi wyraz ciągu
    a = 0
    b = 1
    
    # Lista do przechowywania wyrazów ciągu
    sequence = []

    # Sprawdzamy, czy potrzebujemy przynajmniej jednego lub dwóch wyrazów
    if count >= 1:
        sequence.append(a)
    if count >= 2:
        sequence.append(b)
        
    # Pętla generująca pozostałe wyrazy
    # Zaczynamy od i = 2, ponieważ pierwsze dwa wyrazy są już zainicjowane
    for i in range(2, count):
        # Obliczamy kolejny wyraz (suma dwóch poprzednich)
        next_term = a + b
        sequence.append(next_term)
        
        # Aktualizujemy zmienne dla następnej iteracji
        # Wartość b staje się nowym a, a nowo obliczony next_term staje się nowym b
        a = b
        b = next_term
        
    return sequence

# Uruchomienie programu dla pierwszych 20 wyrazów
NUMBER_OF_TERMS = 20
fib_result = fibonacci_sequence(NUMBER_OF_TERMS)

print(f"\n--- Pierwsze {NUMBER_OF_TERMS} wyrazów ciągu Fibonacciego ---")
# Wyświetlamy wynik w formacie ciągu
print(" ".join(map(str, fib_result)))