def f(n):
    if n <= 0:
        return ""
    
    result_string = ""

    for i in range(1, n + 1):
        result_string += str(i)
    return result_string


# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: n = 11
result1 = f(11)
print(f"f(11) returns \"{result1}\"")

# Przykład 2: n = 4
result2 = f(4)
print(f"f(4) returns \"{result2}\"")