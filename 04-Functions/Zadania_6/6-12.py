def f(n):
    if n <= 0:
        return ""
    
    list = ["*"] * n
    return "/" .join(list)


# --- Przykłady użycia (zgodnie z Sample result) ---

# Przykład 1: n = 4
result1 = f(4)
print(f"f(4) returns \"{result1}\"")

# Przykład 2: n = 1
result2 = f(1)
print(f"f(1) returns \"{result2}\"")