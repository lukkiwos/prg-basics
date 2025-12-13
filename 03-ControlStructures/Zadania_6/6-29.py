import math

def is_prime(num):
    # Sprawdza, czy dana liczba jest liczbą pierwszą.
    # Zgodnie z definicją: liczba pierwsza jest > 1 i dzieli się tylko przez 1 i samą siebie.

    # Sprawdzamy, czy liczba jest mniejsza lub równa 1 (nie jest pierwsza)
    if num <= 1:
        return False
    
    # Krok optymalizacji: wystarczy sprawdzić podzielność do pierwiastka kwadratowego z liczby.
    # Jeśli liczba ma dzielnik większy od swojego pierwiastka, musi mieć też dzielnik mniejszy.
    limit = int(math.sqrt(num)) + 1
    
    # Pętla sprawdzająca podzielność
    # Używamy pętli (zgodnie z instrukcją zadania), aby sprawdzić, 
    # czy liczba jest podzielna przez jakikolwiek inny numer niż 1 i ona sama.
    for i in range(2, limit):
        if num % i == 0:
            # Znaleziono dzielnik inny niż 1 i num, więc to NIE jest liczba pierwsza
            return False
            
    # Jeśli pętla się zakończyła bez znalezienia dzielnika, to jest to liczba pierwsza
    return True

# --- Główna część programu ---

try:
    # Krok 1: Odczytujemy wartość N od użytkownika
    input_n = input("Enter the number of prime numbers (N) you want to find: ")
    N = int(input_n)
    
    if N <= 0:
        print("Please enter a positive number for N.")
    else:
        primes_found = []
        current_number = 2  # Zaczynamy sprawdzanie od pierwszej liczby pierwszej (2)
        
        # Krok 3: Pętla główna: szukamy N liczb pierwszych
        while len(primes_found) < N:
            if is_prime(current_number):
                primes_found.append(current_number)
            
            # Przechodzimy do kolejnej liczby
            current_number += 1

        # Wypisujemy wynik
        print(f"\nThe first {N} prime numbers are:")
        print(" ".join(map(str, primes_found)))

except ValueError:
    print("Invalid input. Please enter a natural number for N.")
except Exception as e:
    print(f"An error occurred: {e}")