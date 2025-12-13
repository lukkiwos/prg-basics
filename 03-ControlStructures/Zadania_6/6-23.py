def multiplication_table(number):
    # Generuje i drukuje tabliczkę mnożenia dla podanej liczby w zakresie 1 do 10.
    
    # Używamy pętli for do iteracji po liczbach od 1 do 10 włącznie
    # range(1, 11) generuje sekwencję 1, 2, 3, ..., 10
    print(f"\nTabliczka mnożenia dla liczby: {number}")
    for i in range(1, 11):
        # Obliczamy wynik mnożenia
        result = number * i
        
        # Wyświetlamy wynik zgodnie z wymaganym formatem
        print(f"{number} x {i} = {result}")

# 1. Odczytujemy liczbę od użytkownika
try:
    # Wczytanie liczby i konwersja na typ integer
    input_num = input("Enter number: ")
    number_to_multiply = int(input_num)
    
    # 2. Wywołanie funkcji generującej tabliczkę
    multiplication_table(number_to_multiply)

except ValueError:
    print("Invalid input. Please enter a whole number.")
except Exception as e:
    print(f"An error occurred: {e}")