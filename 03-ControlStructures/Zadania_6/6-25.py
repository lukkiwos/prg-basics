def print_number_pattern(rows):
    # Generuje wzór liczbowy, gdzie wiersz i powtarza cyfrę i, i razy.
    
    print("--- Pattern result ---")
    
    # Pętla zewnętrzna: dla wierszy (i = cyfra do wydrukowania i liczba powtórzeń)
    for i in range(1, rows + 1):
        
        # Tworzymy ciąg znaków, powtarzając cyfrę i, i razy
        # 1. Konwertujemy i na ciąg znaków (np. 5 -> '5')
        # 2. Powtarzamy ten ciąg i razy (np. '5' * 5 -> '55555')
        # Zapisujemy to w zmiennej line
        line = str(i) * i
        
        # Wypisujemy cały wiersz
        print(line)

# Uruchomienie programu dla wzoru od 1 do 9
print_number_pattern(9)