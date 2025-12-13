def print_bingo_series(start, end):    
    output = []
    
    # Iterujemy przez liczby w zakresie od 1 do 30 (włącznie)
    for number in range(start, end + 1):
        
        # Inicjujemy pusty ciąg dla wyjścia
        result = ""

        is_divisible_by_3 = (number % 3 == 0)
        is_divisible_by_5 = (number % 5 == 0)

        if is_divisible_by_3 and is_divisible_by_5:
            result = "Bingo"
        elif is_divisible_by_3:
            result = "Three"
        elif is_divisible_by_5:
            result = "Five"
        else:
            result = str(number)

        output.append(result)
    
    print(" ".join(output))

# Uruchomienie programu dla zakresu od 1 do 30
print("--- Program BINGO (Liczby 1 do 30) ---")
print_bingo_series(1, 30)