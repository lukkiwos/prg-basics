def f(sentence):
    # Używamy metody replace, aby zastąpić wszystkie wystąpienia spacji (' ')
    # pustym ciągiem znaków ('').
    return sentence.replace(' ', '')

# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: Typowe zdanie
sentence1 = "integrated development environment"
result1 = f(sentence1)
print(f(result1))

# Przykład 2: Dłuższe zdanie (z cytatu)
sentence2 = "A programming language is a system of notation for writing computer programs"
result2 = f(sentence2)
print(f(result2))