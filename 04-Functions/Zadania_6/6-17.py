def f(palindrome):
    # Krok 1: Odwrócenie ciągu.
    # Używamy cięcia w Pythonie [::-1], aby odwrócić ciąg znaków.
    reversed_palindrome = palindrome[::-1]
    
    # Krok 2: Porównanie oryginalnego ciągu z odwróconym.
    return palindrome == reversed_palindrome



# --- Przykłady użycia (zgodnie z Sample result) ---

# Palindrom literowy
result1 = f("radar")
print(f"f('radar') returns {result1}")

# Palindrom z cyframi i znakami (12-11-21 czytane wspak to 12-11-21)
result2 = f("12-11-21")
print(f"f('12-11-21') returns {result2}")

# Nie jest palindromem
result3 = f("book")
print(f"f('book') returns {result3}")