def create_dot_pattern():
    # Tworzy i drukuje wzór geometryczny z kropek.
    
    # 1. Górna połowa (wiersze 1, 2, 3, 4 - rosnąca liczba kropek)
    # Maksymalna liczba kropek (środek) to 7, co odpowiada range(4) dla i=1 do 4
    for i in range(1, 5):
        # Liczba kropek w danym wierszu: 2 * i - 1
        num_dots = 2 * i - 1
        
        # Obliczamy liczbę spacji potrzebnych do wyśrodkowania wzoru
        # Najszerszy wiersz ma 7 znaków (kropek).
        # Spacje = (7 - num_dots) // 2
        num_spaces = (7 - num_dots) // 2
        
        # Tworzymy wiersz: Spacje + Kropki + Spacje
        line = " " * num_spaces + "." * num_dots
        print(line)

    # 2. Dolna połowa (wiersze 5, 6, 7 - malejąca liczba kropek)
    # Zaczynamy od i=3, kończymy na i=1
    for i in range(3, 0, -1):
        # Liczba kropek w danym wierszu: 2 * i - 1
        num_dots = 2 * i - 1
        
        # Obliczamy liczbę spacji potrzebnych do wyśrodkowania wzoru
        num_spaces = (7 - num_dots) // 2
        
        # Tworzymy wiersz
        line = " " * num_spaces + "." * num_dots
        print(line)

# Uruchomienie programu
print("--- Wzór z kropek ---")
create_dot_pattern()