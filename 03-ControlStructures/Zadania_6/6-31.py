import random

def generate_random_integers(count, min_val, max_val):
    """
    Generuje i drukuje zadaną liczbę 'count' losowych liczb całkowitych 
    z zakresu od 'min_val' do 'max_val' (włącznie).
    """
    print(f"--- {count} losowych liczb całkowitych z zakresu [{min_val}, {max_val}] ---")
    
    # Lista do przechowywania wyników (dla czystszego wydruku)
    random_numbers = []
    
    # Pętla wykonująca się 20 razy
    for _ in range(count):
        # Losowanie liczby całkowitej w zakresie od 5 do 10 włącznie
        random_num = random.randint(min_val, max_val)
        random_numbers.append(random_num)
        
    # Drukowanie wszystkich liczb w jednej linii
    print(" ".join(map(str, random_numbers)))

# Uruchomienie programu dla 20 liczb w zakresie 5 do 10
COUNT = 20
MIN = 5
MAX = 10

generate_random_integers(COUNT, MIN, MAX)