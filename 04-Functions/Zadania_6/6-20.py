import math

def is_prime(num):
    if num <= 1:
        return False
    
    # Optymalizacja: Sprawdzamy podzielność tylko do pierwiastka kwadratowego z num
    limit = int(math.sqrt(num)) + 1
    
    for i in range(2, limit):
        if num % i == 0:
            return False
            
    return True

def f(n):
    if n <= 0:
        return "Error: n must be a positive integer"
    
    primes_found = 0
    current_number = 2  # Zaczynamy od pierwszej liczby pierwszej

    # Pętla główna: kontynuujemy, dopóki nie znajdziemy n liczb pierwszych
    while primes_found < n:
        
        if is_prime(current_number):
            primes_found += 1
            
            # Gdy znajdziemy n-tą liczbę, od razu ją zwracamy
            if primes_found == n:
                return current_number
                
        # Sprawdzamy kolejną liczbę
        current_number += 1
        
    # Ten return jest formalny, ponieważ pętla while zwróci wartość
    # gdy primes_found osiągnie n.
    return None 

# --- Przykłady użycia (zgodnie z Sample result) ---

# Pierwsza liczba pierwsza: 2
result1 = f(1)
print(f"f(1) returns {result1}")

# Piąta liczba pierwsza: 11 (2, 3, 5, 7, 11)
result2 = f(5)
print(f"f(5) returns {result2}")

# Dziesiąta liczba pierwsza: 29
result3 = f(10)
print(f"f(10) returns {result3}")