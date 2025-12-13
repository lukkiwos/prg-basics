def f(number1, number2, number3):
    # 1. Znajdowanie największej liczby
    largest = max(number1, number2, number3)
    
    # 2. Znajdowanie najmniejszej liczby
    smallest = min(number1, number2, number3)
    
    # 3. Zwracanie różnicy
    difference = largest - smallest
    return difference

# --- Przykłady użycia ---

result1 = f(7, 4, 9)
print(result1)

result2 = f(2, 12, 8)
print(result2)