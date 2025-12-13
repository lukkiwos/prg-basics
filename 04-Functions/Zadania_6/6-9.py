def f(number):
    current_number = number
    total_sum = 0
    
    # Obsługa przypadku, gdy wejściem jest 0
    if current_number == 0:
        return 0

    # 2. Używamy pętli while do rozbicia liczby na cyfry
    while current_number > 0:
        # Pobieramy ostatnią cyfrę (reszta z dzielenia przez 10)
        digit = current_number % 10
        
        # Dodajemy cyfrę do sumy
        total_sum += digit
        
        # Usuwamy ostatnią cyfrę (całkowite dzielenie przez 10)
        current_number //= 10
        
    return total_sum

if __name__ == "__main__":
    print("--- Testowanie funkcji sum_of_digits(number) ---")

    # Przykładowe testy
    number_1 = 123
    print(f"Suma cyfr liczby {number_1} wynosi: {f(number_1)} (1+2+3=6)")

    number_2 = 9876
    print(f"Suma cyfr liczby {number_2} wynosi: {f(number_2)} (9+8+7+6=30)")

    number_3 = 5
    print(f"Suma cyfr liczby {number_3} wynosi: {f(number_3)} (5)")

    number_4 = 0
    print(f"Suma cyfr liczby {number_4} wynosi: {f(number_4)} (0)")
    
    number_5 = 1001
    print(f"Suma cyfr liczby {number_5} wynosi: {f(number_5)} (1+0+0+1=2)")