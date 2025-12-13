def f(sentence):
    # Krok 1: Dzielenie zdania na słowa.
    # Użycie split() bez argumentów dzieli po białych znakach i ignoruje wielokrotne spacje.
    words = sentence.split()
    
    # Lista do przechowywania pierwszych liter
    acronym_letters = []
    
    # Krok 2 & 3: Iteracja i ekstrakcja pierwszej litery
    for word in words:
        if word:  # Upewniamy się, że słowo nie jest puste
            # Bierzemy pierwszą literę i zamieniamy na wielką (uppercase)
            first_letter = word[0].upper()
            acronym_letters.append(first_letter)
            
    # Krok 4: Połączenie liter w akronim
    acronym = "".join(acronym_letters)
    
    return acronym

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: "Internet of Things" -> "IoT"
result1 = f("Internet of Things")
print(f"f('Internet of Things') returns '{result1}'")

# Przykład 2: "For Your Information" -> "FYI"
result2 = f("For Your Information")
print(f"f('For Your Information') returns '{result2}'")

# Przykład 3: "Python" -> "P"
result3 = f("Python")
print(f"f('Python') returns '{result3}'")

# Przykład 4: "integrated development environment" -> "IDE"
# Zgodnie z przykładem z Zadania 18 (które również dotyczyło zdań)
result4 = f("integrated development environment")
print(f"f('integrated development environment') returns '{result4}'")