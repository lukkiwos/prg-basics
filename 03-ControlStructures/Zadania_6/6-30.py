import random

def generate_lotto_set(min_val, max_val, count):
    """
    Generuje pojedynczy zestaw 'count' unikalnych liczb z zakresu [min_val, max_val].
    """
    # Używamy random.sample, aby wylosować 'count' unikalnych elementów z populacji
    numbers = random.sample(range(min_val, max_val + 1), count)
    # Sortujemy wylosowane liczby dla przejrzystości
    numbers.sort()
    return numbers

def generate_lotto_coupon(num_sets, num_per_set, min_val, max_val):
    """
    Generuje cały kupon loteryjny (num_sets zestawów).
    """
    coupon = []
    # Generujemy określoną liczbę zestawów (wierszy)
    for _ in range(num_sets):
        lotto_set = generate_lotto_set(min_val, max_val, num_per_set)
        coupon.append(lotto_set)
    return coupon

# --- Ustawienia kuponu ---
NUM_SETS = 7      # Liczba zestawów (wierszy)
NUM_PER_SET = 6   # Liczba liczb w każdym zestawie
MIN_NUMBER = 1
MAX_NUMBER = 49

# Generowanie i wyświetlanie kuponu
lotto_coupon = generate_lotto_coupon(NUM_SETS, NUM_PER_SET, MIN_NUMBER, MAX_NUMBER)

print("--- Losowo wygenerowany kupon loteryjny (7 zestawów) ---")
for i, lotto_set in enumerate(lotto_coupon):
    # Wyświetlenie: Zestaw X: Liczby (oddzielone spacjami)
    print(f"{i + 1}: {' '.join(map(str, lotto_set))}")
