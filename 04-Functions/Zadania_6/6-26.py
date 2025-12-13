def f(text):
    # Krok 1: Zamiana ciągu na listę znaków jest niejawna, 
    # gdy używamy metody join() na ciągu.
    
    # Krok 2: Użycie metody join() do połączenia znaków za pomocą '-'
    return '-'.join(text)

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: "University"
result1 = f("University")
print(f"f('University') returns '{result1}'")

# Przykład 2: "UE"
result2 = f("UE")
print(f"f('UE') returns '{result2}'")

# Przykład 3: "x"
result3 = f("x")
print(f"f('x') returns '{result3}'")

# Przykład 4: Pusty ciąg
result4 = f("")
print(f"f('') returns '{result4}'")